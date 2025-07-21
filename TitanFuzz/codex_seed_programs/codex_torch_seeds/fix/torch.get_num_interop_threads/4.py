'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_num_interop_threads\ntorch.get_num_interop_threads()\n'
import torch
import numpy as np
x = torch.randn(2, 3)
y = torch.randn(2, 3)
z = torch.randn(2, 3)
print(torch.get_num_interop_threads())
torch.set_num_interop_threads(5)
print(torch.get_num_interop_threads())