'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_interop_threads\ntorch.set_num_interop_threads(int)\n'
import torch
import torch
x = torch.rand(1, 1, 32, 32, 32, 32)
torch.set_num_interop_threads(1)
y = torch.sum(x)
y.backward()
print(y)