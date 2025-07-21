'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_num_interop_threads\ntorch.get_num_interop_threads()\n'
import torch
import numpy as np
x = torch.rand(10, 10)
print(x)
print(torch.get_num_interop_threads())