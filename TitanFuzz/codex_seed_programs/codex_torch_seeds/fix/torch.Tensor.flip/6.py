'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flip\ntorch.Tensor.flip(_input_tensor, dims)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
_output_tensor = torch.Tensor.flip(_input_tensor, dims=(2,))
print(_input_tensor)
print(_output_tensor)