'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_complex\ntorch.Tensor.is_complex(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
print(torch.Tensor.is_complex(_input_tensor))