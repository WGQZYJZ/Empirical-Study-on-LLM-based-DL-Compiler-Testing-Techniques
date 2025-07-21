'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapaxes\ntorch.Tensor.swapaxes(_input_tensor, axis0, axis1)\n'
import torch
input_tensor = torch.arange(0, 24).view(2, 3, 4)
print('Input tensor: ', input_tensor)
swapaxes_output = input_tensor.swapaxes(0, 2)
print('Swapaxes output: ', swapaxes_output)