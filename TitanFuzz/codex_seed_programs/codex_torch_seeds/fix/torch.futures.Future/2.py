'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.futures.Future\ntorch.futures.Future(*, devices=None)\n'
import torch
import time
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = torch.rand(100, 100)
print('Task 3: Call the API torch.futures.Future')
start = time.time()
futures = []
for i in range(0, 100):
    futures.append(torch.futures.Future())
for i in range(0, 100):
    futures[i].set_result(input_data[i])
end = time.time()
print('Time: ', (end - start))