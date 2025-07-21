'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.smm\ntorch.Tensor.smm(_input_tensor, mat)\n'
import torch
_input_tensor = torch.rand(2, 3)
mat = torch.rand(3, 2)
result = _input_tensor.smm(mat)
print('input tensor:', _input_tensor)
print('mat:', mat)
print('result:', result)