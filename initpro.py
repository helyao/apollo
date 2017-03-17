import pymongo
from config import config, RUN_LEVEL

# [Root]Init MongoDB Client
mg_cl = pymongo.MongoClient(config[RUN_LEVEL].MONGO_HOST, config[RUN_LEVEL].MONGO_PORT)

# *** Configuretion ***
# [Database]Store system information
mg_info_db = mg_cl.info
# [Collection]Store equipment information
mg_equip_coll = mg_info_db.equip
# [Collection]Store user information
mg_user_coll = mg_info_db.user

# *** Data ***
# [Database]Store data
mg_data_db = mg_cl.data
# [Collection]Store atmosphere data
mg_atmos_coll = mg_data_db.atmos

print("Info: start configuration mongodb...")

# *** Clean environment ***
if config[RUN_LEVEL].INIT_DB_CLEAN_CONF:
    mg_equip_coll.remove()
    mg_user_coll.remove()
    print("Suc: clean mongodb configuration.")
if config[RUN_LEVEL].INIT_DB_CLEAN_DATA:
    mg_atmos_coll.remove()
    print("Suc: clean mongodb atmosphere data.")

# *** Insert Configuration ***


