from dbconnection import Database
from controller.ofertadetalle import OfertaDetalle
from preprocessing import clearDataset, remove_tags_html
import pandas as pd


query = """select od.id_ofertadetalle,od.descripcion,
    od.descripcion_normalizada
    from oferta o                    
    inner join oferta_detalle od
    on (o.id_oferta=od.id_oferta)
    where  o.id_estado is null and length(trim(od.descripcion_normalizada))>0
    order by 1 """

if __name__ == '__main__':
    
    # Obteniendo la conexión a la base de datos
     # Actualizando la base de datos
    db = Database()
    
    # Obtener data a tratar
    db.cur.execute(query)
    data = db.cur.fetchall()
    db.close()

    # Convetiendo a dataframe para su tratamiento
    dataset = pd.DataFrame(data, columns=('id','descr','desc_norm'))
    dataset['n_desc_norm'] = clearDataset(dataset, 'descr')
    # dataset['n_desc_norm'] = dataset['n_desc_norm'].apply(remove_tags_html)
    
    # Obteniendo la data que falta actualizar
    dataset_to_update = dataset[dataset['n_desc_norm'] != dataset['desc_norm']]
    
    
    
    # Cerrando la base de datos
    # db.close()


