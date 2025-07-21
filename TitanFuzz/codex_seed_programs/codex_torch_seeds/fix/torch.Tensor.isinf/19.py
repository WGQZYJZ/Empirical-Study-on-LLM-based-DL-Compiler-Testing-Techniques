'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isinf\ntorch.Tensor.isinf(_input_tensor)\n'
import torch
input_tensor = torch.rand(4, 4)
print('The input tensor: ', input_tensor)
output = torch.Tensor.isinf(input_tensor)
print('The result of torch.Tensor.isinf: ', output)