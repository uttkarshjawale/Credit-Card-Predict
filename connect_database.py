from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
         'secure_connect_bundle': 'E:\Credit_Card\Credit_Card_Default_prediction\secure-connect-credit-card.zip'
}
auth_provider = PlainTextAuthProvider('PrNIzEROGXWqyuNTwuqFwvMb', 'hmttwqYm,-ReF7nhae4ttqHxejLLI+nNBJem1xzoAbjid.kPeoQ048GTkuOgZnJZ.I5N,jZcYjnZytc1YvvsGhYUwN,Zh6mT.WcKOBCX4BdYG+EoWE.gE5vD7Fuex70.')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
      print(row[0])
else:
      print("An error occurred.")