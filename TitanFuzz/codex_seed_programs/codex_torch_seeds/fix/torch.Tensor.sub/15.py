'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub\ntorch.Tensor.sub(_input_tensor, other, *, alpha=1)\n'
import torch
_input_tensor = torch.randn(2, 3)
output = torch.Tensor.sub(_input_tensor, _input_tensor)
print(output)