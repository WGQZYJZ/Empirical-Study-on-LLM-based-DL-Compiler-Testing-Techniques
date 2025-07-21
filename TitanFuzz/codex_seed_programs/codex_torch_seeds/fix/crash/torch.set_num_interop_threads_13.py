'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_interop_threads\ntorch.set_num_interop_threads(int)\n'
import torch
x = torch.rand(1000, 1000)
torch.set_num_interop_threads(2)
print(torch.get_num_interop_threads())
y = torch.matmul(x, x)
print(y)