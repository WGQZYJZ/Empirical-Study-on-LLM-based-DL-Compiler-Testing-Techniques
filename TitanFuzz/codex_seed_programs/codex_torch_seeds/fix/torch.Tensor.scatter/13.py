'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.randn(1, 6)
print('input tensor: ', input_tensor)
index = torch.tensor([[4, 1, 2, 5]])
src = torch.tensor([[10, 20, 30, 40]])
output_tensor = torch.Tensor.scatter(input_tensor, 0, index, src)
print('output tensor: ', output_tensor)