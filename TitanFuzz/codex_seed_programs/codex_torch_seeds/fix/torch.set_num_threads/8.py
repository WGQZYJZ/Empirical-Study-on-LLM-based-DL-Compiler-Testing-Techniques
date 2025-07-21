'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_threads\ntorch.set_num_threads(int)\n'
import torch
x = torch.rand(1000, 1000)
y = torch.rand(1000, 1000)
torch.set_num_threads(8)
print('Number of threads: ', torch.get_num_threads())
print('Number of interop threads: ', torch.get_num_interop_threads())
print('Number of threads: ', torch.get_num_threads())
print('Number of interop threads: ', torch.get_num_interop_threads())