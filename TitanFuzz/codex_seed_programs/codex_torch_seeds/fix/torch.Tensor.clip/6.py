'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clip\ntorch.Tensor.clip(_input_tensor, min=None, max=None)\n'
import torch
import numpy as np
input_tensor = torch.randn([1, 3, 224, 224])
output_tensor = torch.Tensor.clip(input_tensor, min=0.0, max=1.0)
print('The input tensor is:', input_tensor)
print('The output tensor is:', output_tensor)