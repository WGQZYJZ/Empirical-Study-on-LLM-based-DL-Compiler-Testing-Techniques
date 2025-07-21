'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numpy\ntorch.Tensor.numpy(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 3, 224, 224)
_output_tensor = _input_tensor.numpy()
print(_output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.permute\ntorch.Tensor.permute(_input_tensor, _dims)\n'
import torch
_input_tensor = torch.randn(1, 3, 224, 224)
_dims = (0, 2, 3, 1)
_output_tensor = _input_tensor.permute(_dims)
print(_output_tensor)