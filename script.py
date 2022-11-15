from beautifultable import BeautifulTable
import boto3

table = BeautifulTable()
table.columns.header = ["Count", "Function Name", "Reserved Concurrency"]

region="us-west-2"
# region="us-east-1"

lambda_client = boto3.client('lambda', region_name=region)
count = 0

paginator = lambda_client.get_paginator('list_functions')
page_iterator = paginator.paginate()

for items in page_iterator:
    for functions in items['Functions']:
        count = count+1
        response = lambda_client.get_function_concurrency(
            FunctionName=functions['FunctionName']
        )
        try:
            print(count,
                functions['FunctionName'], 
                response['ReservedConcurrentExecutions'],
                sep=";"
            )
            # table.rows.append([
            #     f"{count}", 
            #     f"{functions['FunctionName']}",
            #     f"{response['ReservedConcurrentExecutions']}"
            # ])
        except Exception as e:
            print(count,
                functions['FunctionName'],
                "Unreserved",
                sep=";"
            )
            # table.rows.append([
            #     f"{count}",
            #     f"{functions['FunctionName']}",
            #     "Unreserved"
            # ])

# print(table)
