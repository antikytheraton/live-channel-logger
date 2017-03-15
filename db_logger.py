import psycopg2
import time


class DatabaseLogger:
    conn = None
    cursor = None

    def __init__(self, host, name, user, password):
        self.conn = psycopg2.connect(host=host, dbname=name, user=user, password=password)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def close(self):
        ''' Closes all cnnections to the DB '''
        self.cursor.close()
        self.conn.close()
    
    def track_exists(self, track_id, batch):
        ''' Checks if the channel already exists in the DB and Batch to
            avoid duplicates.'''
        cur = self.conn.cursor()
        cur.execute("SELECT channel FROM stream_log WHERE channel = %s AND batch = %s", (track_id,batch))
        return cur.fetchone() is not None

    def log_stream(self, batch, stream):
        ''' Logs the datat taken from the API into the DB'''

        if 'status' not in stream['channel']:
            stream['channel']['status'] = None
        elif stream['channel']['status'] and len(stream['channel']['status']) > 128:
            stream['channel']['status'] = stream['channel']['status'][:128]
        if 'game' not in stream['channel']:
            stream['channel']['game'] = None
        elif stream['channel']['game'] and len(stream['channel']['game']) > 64:
            stream['channel']['game'] = stream['channel']['game'][:64]

        if self.cursor.closed:
            return
        
        try:
            self.cursor.execute("INSERT INTO stream_log (batch, channel, title, game, viewers, date) "
                                "VALUES (%s, %s, %s, %s, %s, %s)",
                                (batch, stream['channel']['name'],
                                stream['channel']['status'],
                                stream['channel']['game'],
                                int(stream['viewers']),
                                current_time_in_milli()))
        except psycopg2.DataError as e:
            print e
            print stream

def current_time_in_milli():
    ''' Gets the time in mili to  '''
    return int(round(time.time() * 1000))
