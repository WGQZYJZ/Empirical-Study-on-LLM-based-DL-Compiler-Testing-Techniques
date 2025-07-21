'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub_\ntorch.Tensor.sub_(_input_tensor, other, *, alpha=1)\n'
import torch
_input_tensor = torch.randn(4, 4)
_output_tensor = torch.Tensor.sub_(_input_tensor, other=5)
print(_output_tensor)