'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.squeeze\ntorch.Tensor.squeeze(_input_tensor, dim=None)\n'
import torch
input_tensor = torch.randn(3, 1, 5, 1)
squeeze_tensor = input_tensor.squeeze(dim=1)
print('squeeze_tensor: ', squeeze_tensor)