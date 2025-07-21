'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_interop_threads\ntorch.set_num_interop_threads(int)\n'
import torch
import time
torch.set_num_interop_threads(4)
torch.set_num_threads(4)
print('Number of threads before: ', torch.get_num_threads())
print('Number of interop threads before: ', torch.get_num_interop_threads())
x = torch.tensor([[1, 2], [3, 4]])
y = torch.matmul(x, x)