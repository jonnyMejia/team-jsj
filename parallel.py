# Python Libraries
import time
import multiprocessing
import psutil

# Third Python libraries
import pandas as pd

# Local libraries
from dbconnection import Database
from preprocessing import clearDataset
from controller.ofertadetalle import OfertaDetalle

query = """select od.id_ofertadetalle,od.descripcion,
    od.descripcion_normalizada
    from oferta o                    
    inner join oferta_detalle od
    on (o.id_oferta=od.id_oferta)
    where  o.id_estado is null and length(trim(od.descripcion_normalizada))>0
    order by 1 """

def update_dataset(data):
    db = Database()
    for oferta_id, n_descr_norm in data:
        OfertaDetalle().update(db, n_descr_norm.upper(), oferta_id)
    db.close()


if __name__ == '__main__':
    NUM_WORKERS = psutil.cpu_count(logical=False)
    

    # Actualizando la base de datos
    db = Database()
    
    # Obtener data a tratar
    db.cur.execute(query)
    data = db.cur.fetchall()
    db.close()

    # Convetiendo a dataframe para su tratamiento
    dataset = pd.DataFrame(data, columns=('id','descr','desc_norm'))
    dataset['n_desc_norm'] = clearDataset(dataset, 'descr')

    # Cargando data que falta actualizar
    dataset_to_update = dataset[dataset['n_desc_norm'] != dataset['desc_norm']]

    start_time = time.time()
    split = round(len(dataset)/NUM_WORKERS + 0.5)
    
    processes = [multiprocessing.Process(target=update_dataset, args=(dataset_to_update.iloc[x:x+split,[0, 3]].values, )) 
                 for x in range(0,len(dataset_to_update), split)]
    [process.start() for process in processes]
    [process.join() for process in processes]

    end_time = time.time()
    
    print("Parallel time=", end_time - start_time)
    

