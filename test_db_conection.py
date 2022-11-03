import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://yulsepm:<Yuli2110075>@mintic4.ktjkavc.mongodb.net/academic_db?retryWrites=true&w=majority",
    tlsCAFile=ca
)
db = client.test
print(db)

data_base = client['academic_db']
print(data_base.list_collection_names())

student = data_base.get_collection('student')
all_student = student.find({})
