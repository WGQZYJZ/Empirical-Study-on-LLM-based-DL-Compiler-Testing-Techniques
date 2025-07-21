'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.futures.Future\ntorch.futures.Future(*, devices=None)\n'
import torch
import time
import torch
import time
input_data = torch.rand(100, 100)
future = torch.futures.Future(devices=None)
start_time = time.time()
output_data = input_data.mm(input_data)
end_time = time.time()
print('Elapsed time: {:.2f}'.format((end_time - start_time)))
print('Elapsed time: {:.2f}'.format((end_time - start_time)))
print('Elapsed time: {:.2f}'.format((end_time - start_time)))
print('Elapsed time: {:.2f}'.format((end_time - start_time)))