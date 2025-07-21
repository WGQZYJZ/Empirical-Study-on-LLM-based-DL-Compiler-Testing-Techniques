'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.squeeze\ntorch.Tensor.squeeze(_input_tensor, dim=None)\n'
import torch
input_tensor = torch.randn(2, 1, 2, 1, 2)
print('The input tensor is: ', input_tensor)
squeeze_tensor = input_tensor.squeeze()
print('The squeeze tensor is: ', squeeze_tensor)
squeeze_tensor = input_tensor.squeeze(dim=1)
print('The squeeze tensor is: ', squeeze_tensor)
squeeze_tensor = input_tensor.squeeze(dim=2)
print('The squeeze tensor is: ', squeeze_tensor)