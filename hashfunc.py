class HashTable:

    def __init__(self,size):
        self.size = size
        self.hash_table=self.create_bucket()

    def create_bucket(self):
        return [[] for _ in range(self.size)]

    def set_val(self,key,value):
        hashed_key=hash(key)%self.size
        bucket=self.hash_table[hashed_key]
        found_key = False
        for index , record in enumerate(bucket):
            record_key,record_value=record
            if record_key==key:
                found_key=True
                break
        if found_key:
            bucket[index]= (key,value)
        else:
            bucket.append((key,value))

    def get_val(self, key):
        hashed_key=hash(key)%self.size
        bucket=self.hash_table[hashed_key]
        found_key = False
        for index , record in enumerate(bucket):
            record_key,record_value=record
            if record_key==key:
                found_key=True
                break
        if found_key:
            return record_value

    def del_val(self,key):
        hashed_key=hash(key)%self.size
        bucket=self.hash_table[hashed_key]
        found_key = False
        for index , record in enumerate(bucket):
            record_key,record_value=record
            if record_key==key:
                found_key=True
                break
        if found_key:
            return bucket.pop(index)
        else:
            return "nill"


    def __str__(self):
        return "".join(str(item) for item in self.hash_table)



hashtable=HashTable(10)
with open("hashdata.txt") as f:
    for line in f:
        key , value =line.split(":")
        hashtable.set_val(key,value)
        hashtable.set_val("gowtham","walk alone")
print(hashtable.del_val("gowtham"))

print(hashtable)
