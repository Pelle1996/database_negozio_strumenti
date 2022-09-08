

#comandi terminale -> testdb-# \d
#psql postgres://francesco@localhost:5433/francesco

from select import select
import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'francesco'
username = 'francesco'
pwd = 'ciao'
port_id = 5433
conn = None

##################### FUNZIONE INSERT STRUMENTO #############################################

def inserisciStrumento():
    
            codice_v=input("Inserisci il codice strumento: ")
            categoria_v=input("inserisci categoria: ")
            modello_v=input("Inserisci il modello: ")
            azienda_v=input("Inserisci la marca: ")
            prezzo_v=input("Inserisci il prezzo: ")
            n_pezzi_disp_v = input("Inserisci il numero di unità disponibili: ")

            # INSERT Strumento
            insert_script  = 'INSERT INTO strumento (codice_str,categoria,modello,azienda,prezzo,n_pezzi_disp) VALUES (%s,%s,%s,%s,%s,%s)'
            insert_values = [(codice_v,categoria_v,modello_v,azienda_v,prezzo_v,n_pezzi_disp_v)]
            for record in insert_values:
                cur.execute(insert_script, record)
        
def inserisciVendita():
            codice_v=input("Inserisci il codice vendita: ")
            codice_str=input("inserisci codice strumento: ")
            prezzo_v=input("Inserisci il prezzo di vendita: ")
            data=input("Inserisci la data: ")
            cf=input("Inserisci il cf di chi ha effettuato la vendita: ")
            


            # INSERT vendita
            insert_script  = 'INSERT INTO vendite (codice_vendita,codice_str,prezzo_vendita,data,cf) VALUES (%s,%s,%s,%s,%s)'
            insert_values = [(codice_v,codice_str,prezzo_v,data,cf)]
            for record in insert_values:
                cur.execute(insert_script, record)

def inserisciSpedizione():
            n_track=input("Inserisci il tracking number: ")
            codice_vr=input("inserisci codice vendita: ")
            stato_sp=input("Inserisci lo stato della spedizionevendita: ")
            indirizzo=input("Inserisci la indirizzo: ")
        
            # INSERT spedizione
            insert_script  = 'INSERT INTO spedizione (tracking,codice_vendita,stato_spedizione,indirizzo) VALUES (%s,%s,%s,%s)'
            insert_values = [(n_track,codice_vr,stato_sp,indirizzo)]
            for record in insert_values:
                cur.execute(insert_script, record)           


def licenziamento(cf):
            #DELETE
            delete_script = 'DELETE FROM dipendente WHERE cf = (%s)'
            delete_record = (cf,)
            cur.execute(delete_script, delete_record)


def rimuovi_strumento(id):
            #DELETE
            delete_script = 'DELETE FROM strumento WHERE codice_str = (%s)'
            delete_record = (id,)
            cur.execute(delete_script, delete_record)



##################### PROGRAMMA #############################################
try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:


           #ELIMINA TABELLE

            cur.execute('DROP TABLE IF EXISTS dipendente')            
            cur.execute('DROP TABLE IF EXISTS vendite')
            cur.execute('DROP TABLE IF EXISTS spedizione')
            cur.execute('DROP TABLE IF EXISTS strumento')
            



            ###################   TABELLE   ###################   

            #TABELLA Strumento
            create_script = ''' CREATE TABLE IF NOT EXISTS strumento (
                                    codice_str varchar(11) PRIMARY KEY,
                                    categoria varchar(11) NOT NULL,
                                    modello varchar(50) NOT NULL,
                                    azienda varchar(50) NOT NULL,
                                    prezzo decimal(6,2) NOT NULL,
                                    n_pezzi_disp int NOT NULL)'''
            cur.execute(create_script)

            #TABELLA Dipendente
            create_script = ''' CREATE TABLE IF NOT EXISTS dipendente (
                                    cf varchar(20) PRIMARY KEY,
                                    nome varchar(20) NOT NULL,
                                    cognome varchar(20) NOT NULL,
                                    indirizzo varchar(50) NOT NULL,
                                    mansione varchar(20) NOT NULL,
                                    stipendio int NOT NULL
                                    ) '''
            cur.execute(create_script)



             #TABELLA Vendite
            create_script = ''' CREATE TABLE IF NOT EXISTS vendite (
                                    codice_vendita varchar(11) PRIMARY KEY,
                                    codice_str varchar(11) NOT NULL,
                                    prezzo_vendita decimal(6,2) NOT NULL,
                                    data date NOT NULL,
                                    cf varchar(20) NOT NULL )'''
            cur.execute(create_script)

            


            #TABELLA Spedizione
            create_script = ''' CREATE TABLE IF NOT EXISTS spedizione (
                                    tracking varchar(11) PRIMARY KEY,
                                    codice_vendita varchar(11) NOT NULL,
                                    stato_spedizione varchar(20) NOT NULL,
                                    indirizzo varchar(50) NOT NULL)'''
            cur.execute(create_script)




#######################################################################


            # INSERT DIPENDENTI
            insert_script  = 'INSERT INTO dipendente (cf,nome,cognome,indirizzo,mansione,stipendio) VALUES (%s, %s, %s,%s, %s, %s)'
            insert_values = [('PLLFNC96M02H620Q', 'Francesco','Pellegrin','via pascoli 1','tecnico',1200),('FLLRSSC97M02H620Q', 'Filippo', 'Rossi','via rossi 23','commesso',1100),('ALLRSSC97M02H620Q', 'Alessandro', 'Riva','via bolle','commesso',1300),('LUBILRSS99M02H620Q', 'Luca', 'Bianchi','via corse','commesso',1300)]
            for record in insert_values:
                cur.execute(insert_script, record)

            # INSERT DIPENDENTI
            insert_script  = 'INSERT INTO vendite (codice_vendita,codice_str,prezzo_vendita,data,cf) VALUES (%s,%s,%s,%s,%s)'
            insert_values = [('123V','STR123',1200,'02-08-2022','PLLFNC96M02H620Q'),('1113V','STR223',1500,'02-09-2022','PLLFNC96M02H620Q'),('23V','TR123',1200,'05-08-2022','PLLFNC96M02H620Q')]
            for record in insert_values:
                cur.execute(insert_script, record)


            insert_script  = 'INSERT INTO spedizione (tracking,codice_vendita,stato_spedizione,indirizzo) VALUES (%s,%s,%s,%s)'
            insert_values = [('TR123','1113V','in_consegna','via dei mille 12'),('TR223','123V','spedito','via dei mille 21')]
            for record in insert_values:
                cur.execute(insert_script, record)  

            # INIZIO
            azione = input("Cosa vuoi fare?:   ")
            while(azione != "stop"):

                #inserisci strumento    (FUNZIONA)
                if(azione=="inserisci strumento"):
                    inserisciStrumento()
                    print("--------------(strumento inserito)----------------\n")

                #inserisci strumento    (FUNZIONA)
                if(azione=="vendita"):
                    inserisciVendita()
                    print("--------------(vendita inserita)----------------\n")


                #inserisci spedizione    ()
                if(azione=="spedisci"):
                    inserisciSpedizione()
                    print("--------------(spedizione inserita)----------------\n")

                #update stipendio  (FUNZIONA)
                if(azione=="modifica stipendio"):
                    chi = input("A chi vuoi aumentare lo stipendio?:   ")
                    aumento = input("Di quanto vuoi aumentare lo stipendio?:   ")
            
                    update_script = 'UPDATE dipendente SET stipendio = stipendio + (%s) WHERE dipendente.cf= (%s)' 
                    insert_values = [(aumento, chi)]
                    for record in insert_values:
                        cur.execute(update_script, record)
                    print("--------------(aumento inserito)----------------\n")

                                #update stipendio  (FUNZIONA)
                if(azione=="modifica spedizione"):
                    track_id = input("inserisci il tracking number della spedizione che vuoio modificare: ")
                    new_state = input("nuovo stato:   ")
                    
            
                    update_script = 'UPDATE spedizione SET stato_spedizione =  (%s) WHERE tracking= (%s)' 
                    insert_values = [(new_state, track_id)]
                    for record in insert_values:
                        cur.execute(update_script, record)
                    print("--------------(aggiornamento inserito)----------------\n")


                #delete dipendente  (FUNZIONA)
                if(azione=="licenziamento"):
                    cf = input("inserisci il codice fiscale del dipendente da rimuovere: ")
                    licenziamento(cf)

                
                #ricerca strumento
                if(azione=="ricerca strumento"):

                    mod = input("inserisci il modello dello strumento da cercare: ")
                    search_script=('SELECT * FROM STRUMENTO WHERE modello = (%s)')
                    insert_values = (mod,)
                    cur.execute(search_script, insert_values)
                    for record in cur.fetchall():
                        print(record['codice_str','modello','azienda','prezzo','n_pezzi_disp'])
                    
                    print("--------------(strumenti corrispondenti al modello inserito)----------------\n")

                #numero vendite dipendente strumento
                if(azione=="vendite dipendente"):

                    cf_s = input("inserisci il cf del dipendente per visualizzare il numero di vendite effettuate: ")
                    search_script=('SELECT COUNT(*) FROM VENDITE WHERE cf = (%s)')
                    insert_values = (cf_s,)
                    cur.execute(search_script, insert_values)
                    for record in cur.fetchall():
                       print(record)
                    
                    print("------------------------------\n")

                #ricerca vendita
                if(azione=="ricerca vendita"):

                    mod = input("inserisci il codice vedita: ")
                    search_script=('SELECT * FROM VENDITE WHERE codice_vendita = (%s)')
                    insert_values = (mod,)
                    cur.execute(search_script, insert_values)
                    for record in cur.fetchall():
                        print(record['codice_vendita','codice_str','prezzo_vendita','data','cf'])
                    
                    print("--------------(strumenti corrispondenti al modello inserito)----------------\n")

                if(azione=="dipendenti"):
                    cur.execute('SELECT * FROM DIPENDENTE')
                    for record in cur.fetchall():
                        print(record['nome'], record['cognome'],record['stipendio'])

                if(azione=="ricerca"):
                    #prodotto = input("Inserisci il codice vendita: ")
                    stato = input("stato spedizione: ")
                    join_script=('SELECT * FROM spedizione JOIN vendite ON vendite.codice_vendita = spedizione.codice_vendita WHERE spedizione.stato_spedizione = (%s)')
                    insert_values = (stato,)
                    cur.execute(join_script,insert_values)
                    for record in cur.fetchall():
                        print(record['codice_vendita'],record['codice_str'], record['prezzo_vendita'],record['data'],record['cf'],record['stato_spedizione'],record['tracking'])

                    print("--------------(spedizione e prodotto visualizzati)----------------\n")                  


                
                azione = input("Cosa vuoi fare?:   ")






        


except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()