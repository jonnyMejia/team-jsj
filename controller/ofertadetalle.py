import psycopg2


class OfertaDetalle:


    def update(self, database, descr_norm, ofertadetalle_id):
        
        try:
            query = "UPDATE OFERTA_DETALLE SET descripcion_normalizada=%s WHERE id_ofertadetalle=%s"

            database.cur.execute(query, (descr_norm, ofertadetalle_id))

            database.conn.commit()
        except (Exception, psycopg2.Error) as error:
            database.cur.execute("ROLLBACK")
            database.conn.commit()
            print("Error in updating the data:", error, 'Con ID : ', ofertadetalle_id )
                