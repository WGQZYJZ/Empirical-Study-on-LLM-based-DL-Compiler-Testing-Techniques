'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.movedim\ntorch.Tensor.movedim(_input_tensor, source, destination)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('Input tensor: ', input_tensor)
print('Output tensor: ', input_tensor.movedim(0, 2))
print('Output tensor: ', input_tensor.movedim(1, 2))
print('Output tensor: ', input_tensor.movedim(2, 0))
print('Output tensor: ', input_tensor.movedim(2, 1))