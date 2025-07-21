'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
_input_tensor = torch.randn(4, 4, 4)
dim = 1
index = torch.tensor([0, 1, 2, 3])
src = torch.randn(4, 4, 4)
_output_tensor = torch.Tensor.scatter(_input_tensor, dim, index, src)
print(_output_tensor)