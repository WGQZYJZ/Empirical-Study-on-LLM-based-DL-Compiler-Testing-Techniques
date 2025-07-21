'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_threads\ntorch.set_num_threads(int)\n'
import torch
import time
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = np.random.rand(1000, 1000)
print('Task 3: Call the API torch.set_num_threads')
torch.set_num_threads(1)
print('Task 4: Call the API torch.mm')
start = time.time()
torch.mm(torch.tensor(input_data), torch.tensor(input_data))
end = time.time()
print(('Time cost: %s' % (end - start)))