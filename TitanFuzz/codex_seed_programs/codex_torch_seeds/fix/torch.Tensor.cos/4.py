'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cos\ntorch.Tensor.cos(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 3)
cos_output = torch.Tensor.cos(_input_tensor)
print(cos_output)