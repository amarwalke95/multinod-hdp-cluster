import boto3
import time
time.sleep(600)
l=["Namenode","Datanode1","Datanode2"]
p={}
client = boto3.client('ec2',region_name='us-east-1')
response = client.describe_instances()				
for r in response['Reservations']:
	for i in r['Instances']:
		for j in i['Tags']:
			if j[u'Key']=="Name":
				p[j[u'Value']]=i['PrivateDnsName']				
p1={}				
for i in p:
	if i in l:
		p1[i]=p[i]
f=open("/home/ec2-user/hostmapping.json",'r')
data=f.read()
f.close()
data=data.replace("Namenode",p1['Namenode'])
data=data.replace("Datanode1",p1['Datanode1'])
data=data.replace("Datanode2",p1['Datanode2'])
f=open("/home/ec2-user/hostmapping.json",'w')
f.write(data)
f.close()



		
		

			
			
			
			
			
			
			
			
			
			
			
			
			
		
	



	