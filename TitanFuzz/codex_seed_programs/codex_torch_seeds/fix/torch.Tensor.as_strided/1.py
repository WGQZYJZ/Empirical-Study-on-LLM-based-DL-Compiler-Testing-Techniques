'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.as_strided\ntorch.Tensor.as_strided(_input_tensor, size, stride, storage_offset=0)\n'
import torch
import numpy as np
input_tensor = torch.arange(0, 10)
print(input_tensor)
out_tensor = torch.Tensor.as_strided(input_tensor, size=(2, 5), stride=(5, 1))
print(out_tensor)