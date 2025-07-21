'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('_input_tensor: ', _input_tensor)
dim = 0
index = torch.tensor([1, 0])
src = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
output = torch.Tensor.scatter(_input_tensor, dim, index, src)
print('output: ', output)