'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp_\ntorch.Tensor.clamp_(_input_tensor, min=None, max=None)\n'
import torch
data = torch.randn(1, 1, 3, 3)
print('The input data is: \n', data)
data.clamp_(min=0, max=2)
print('The output data is: \n', data)