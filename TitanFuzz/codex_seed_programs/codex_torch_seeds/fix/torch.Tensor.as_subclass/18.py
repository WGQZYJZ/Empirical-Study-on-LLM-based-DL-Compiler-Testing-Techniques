'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.as_subclass\ntorch.Tensor.as_subclass(_input_tensor, cls)\n'
import torch
input_tensor = torch.randn(1, 2, 3, 4)
cls = torch.FloatTensor
_input_tensor = input_tensor.as_subclass(cls)
print(_input_tensor)