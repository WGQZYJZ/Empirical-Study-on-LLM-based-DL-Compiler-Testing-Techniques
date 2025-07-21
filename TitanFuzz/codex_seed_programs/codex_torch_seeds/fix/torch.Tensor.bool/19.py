'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bool\ntorch.Tensor.bool(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import numpy as np
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
output_tensor = torch.Tensor.bool(input_tensor)
print(output_tensor)