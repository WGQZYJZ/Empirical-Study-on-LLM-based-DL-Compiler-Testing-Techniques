'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill_\ntorch.Tensor.index_fill_(_input_tensor, dim, index, value)\n'
import torch
import numpy as np
input_tensor = torch.randn(2, 3, 4)
print(input_tensor)
input_tensor.index_fill_(0, torch.tensor([0, 1]), 1)
print(input_tensor)