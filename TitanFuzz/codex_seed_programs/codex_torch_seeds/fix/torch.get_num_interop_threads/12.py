'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_num_interop_threads\ntorch.get_num_interop_threads()\n'
import torch
X = torch.rand(1000, 1000)
Y = torch.rand(1000, 1000)
print(torch.get_num_interop_threads())