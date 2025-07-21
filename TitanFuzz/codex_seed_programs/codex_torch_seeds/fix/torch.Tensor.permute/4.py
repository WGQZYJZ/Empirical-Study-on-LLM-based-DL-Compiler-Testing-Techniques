'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.permute\ntorch.Tensor.permute(_input_tensor, *dims)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
_output_tensor = _input_tensor.permute(2, 0, 1)
print(_output_tensor)