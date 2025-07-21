'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histc\ntorch.Tensor.histc(_input_tensor, bins=100, min=0, max=0)\n'
import torch
import numpy as np
input_data = torch.randn(1000)
histc_result = input_data.histc(bins=100, min=0, max=0)
print(histc_result)