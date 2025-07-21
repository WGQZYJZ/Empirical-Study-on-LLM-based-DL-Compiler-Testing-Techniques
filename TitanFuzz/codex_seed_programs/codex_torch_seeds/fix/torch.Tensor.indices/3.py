'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.indices\ntorch.Tensor.indices(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.randn(2, 3, 4, 5)
output_tensor = input_tensor.indices()
print(output_tensor)