'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to\ntorch.Tensor.to(_input_tensor, *args, **kwargs)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
_output_tensor = _input_tensor.to(dtype=torch.int32)
print(_output_tensor)