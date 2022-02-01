import random
import string

user_ids = list(range(1, 9))


def generate_message() -> dict:
    random_user_id = random.choice(user_ids)
    return {
        "eventId":"REMEDY-1312312312",
        "eventTime":"1/18/2022 3:45:27 PM",
        "eventType":"TicketCreateEvent",
        "event":{
            "ticket":{
            "id": f"INC00000771716{random_user_id}",
            "source":"Remedy",
            "relatedParty":[
                {
                "role":"Resource",
                "name":"ResourceName",
                "additionalData":[
                    {
                    "key":"Empresa Asignada",
                    "value":"value"
                    },
                    {
                    "key":"Organizacion de Soporte",
                    "value":"value"
                    },
                    {
                    "key":"Grupo Remitente",
                    "value":"value"
                    }
                ]
                },
                {
                "role":"Leader",
                "name":"Cliente",
                "additionalData":[
                    {
                    "key":"Empresa1",
                    "value":"empresaName1"
                    },
                    {
                    "key":"Empresa2",
                    "value":"empresaName2"
                    }
                ]
                }
            ],
            "relatedPlace":{
                "address":{
                "region":"LIMA"
                }
            },
            "description":"test arbol",
            "severity":"",
            "product":{
                "name":"Categor\\xc3\\xada de producto de Resoluci\\xc3\\xb3n-producto",
                "additionalData":[
                {
                    "key":"Nivel 1",
                    "value":"ACCESO BAF"
                },
                {
                    "key":"Nivel 2",
                    "value":"RED DE ACCESO"
                },
                {
                    "key":"Nivel 3",
                    "value":"DSLAM"
                }
                ]
            },
            "priority":"0",
            "type":"type",
            "channel":[
                {
                "name":"VISOR"
                }
            ],
            "status":"assigned",
            "note":[
                {
                "date":"1/18/2022 3:45:27 PM",
                "author":"n0inetum01",
                "text":"Prioridad: CLASICO||Masiva: NO||Gestor: HUAWEI U2020 ACCESO||Elemento: EBC||Nombre elemento: LO725U_AEROPUERTO_IQUITOS||Alarma: RF Unit Maintenance Link Failure||Descripci\\xc3\\xb3n de Alarma: ||ID Sitio (planta interna): LO00059||Departamento: LORETO||Fecha y hora de alarma: 17/01/2022 12:00||Tecnolog\\xc3\\xada: 4G"
                }
            ],
            "creationDate":"1/18/2022 3:45:27 PM",
            "reportedDate":"1/18/2022 3:45:27 PM",
            "relatedObject":[
                {
                "involvement":"Ticket de averia",
                "additionalData":[
                    {
                    "key":"Estado",
                    "value":"LIQUIDADA"
                    }
                ]
                }
            ],
            "additionalData":[
                {
                "key":"Estado del ticket en el sistema comercial",
                "value":"COMPLETADO"
                }
            ]
            }
        }
        }
# Pruebas
if __name__ == '__main__':
    print(generate_message())
