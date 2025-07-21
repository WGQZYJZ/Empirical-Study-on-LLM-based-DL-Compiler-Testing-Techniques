'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.apply_\ntorch.Tensor.apply_(_input_tensor, callable)\n'
import torch
_input_tensor = torch.randn(2, 3)
print(_input_tensor)
_input_tensor.apply_((lambda x: (x * 2)))
print(_input_tensor)