'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.std\ntorch.Tensor.std(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
_input_tensor = torch.rand(4, 4)
print('Input tensor: \n', _input_tensor)
print('Standard deviation: ', _input_tensor.std())