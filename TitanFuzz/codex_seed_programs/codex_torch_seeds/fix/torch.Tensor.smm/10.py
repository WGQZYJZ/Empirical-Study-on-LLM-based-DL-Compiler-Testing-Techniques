'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.smm\ntorch.Tensor.smm(_input_tensor, mat)\n'
import torch
_input_tensor = torch.rand(3, 4)
mat = torch.rand(4, 5)
output_tensor = _input_tensor.smm(mat)
print(output_tensor)