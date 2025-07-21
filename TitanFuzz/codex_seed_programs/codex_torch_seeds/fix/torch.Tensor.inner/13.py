'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inner\ntorch.Tensor.inner(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(2, 3)
other = torch.randn(3)
inner_product = _input_tensor.inner(other)
print(inner_product)