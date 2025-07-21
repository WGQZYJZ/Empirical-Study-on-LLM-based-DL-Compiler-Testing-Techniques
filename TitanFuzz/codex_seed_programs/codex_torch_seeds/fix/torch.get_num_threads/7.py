'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_num_threads\ntorch.get_num_threads()\n'
import torch
x = torch.rand(10000, 10000)
y = torch.rand(10000, 10000)
print(torch.get_num_threads())
torch.set_num_threads(8)
print(torch.get_num_threads())
z = torch.matmul(x, y)
print(z)