'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unbind\ntorch.Tensor.unbind(_input_tensor, dim=0)\n'
import torch
input_tensor = torch.randint(0, 10, (2, 3, 4))
print('input_tensor: ', input_tensor)
print('\noutput_tensor: ', input_tensor.unbind(dim=1))