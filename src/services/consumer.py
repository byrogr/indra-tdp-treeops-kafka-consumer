import json
import os

import pymysql.cursors

from dotenv import load_dotenv

load_dotenv()


def preparedNoteField(note):
    arrNoteText = note.split('||')
    arrItemNote = map(lambda i: i.split(':'), arrNoteText)
    print(arrItemNote)


def saveTicketRaw(event):
    conn = pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        cursorclass=pymysql.cursors.DictCursor
    )
    ticket = event['event']['ticket']
    co_ticket = ticket['id']
    eventId = event['eventId']
    eventTime = event['eventTime']
    eventType = event['eventType']
    ticket_detalle = json.dumps(ticket)
    #ticket_notes = preparedNoteField(ticket['note'][0]['text'])
    data = (co_ticket, eventId, eventTime, eventType, ticket_detalle)
    with conn:
        with conn.cursor() as cursor:
            sqlWhere = "SELECT * FROM remedy_tickets_raw WHERE co_ticket = %s"
            cursor.execute(sqlWhere, co_ticket)
            result = cursor.fetchone()
            print(result)
            if result is not None:
                sqlUpd = "UPDATE remedy_tickets_raw SET ticket_detalle = %s WHERE co_ticket = %s"
                cursor.execute(sqlUpd, (ticket_detalle, co_ticket))
            else:
                sqlIns = "INSERT INTO remedy_tickets_raw (co_ticket, eventId, eventTime, eventType, ticket_detalle) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sqlIns, data)
        conn.commit()
