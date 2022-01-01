import mysql.connector

def interact_db(query, query_type: str):
    return_value = False

    #the conection to our DB - commit
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='assignment10',
                                         port='3307')

    #pointer to the DB - query
    cursor=connection.cursor(named_tuple=True)
    cursor.execute(query)

    #two type of query:
    #commit - to insert value (the same in git)
    #sql commands - insert, update, delete
    #fatch - to extract data/value.
    # sql commands - select

    if query_type=='commit':
        connection.commit()
        return_value=True

    if query_type=='fetch':
        query_result=cursor.fetchall()
        return_value=query_result

    connection.close()
    cursor.close()
    return return_value
