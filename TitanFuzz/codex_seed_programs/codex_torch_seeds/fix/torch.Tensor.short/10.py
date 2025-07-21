'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.short\ntorch.Tensor.short(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import numpy as np
input_tensor = torch.randn(3, 5)
output_tensor = input_tensor.short()
print(input_tensor)
print(output_tensor)