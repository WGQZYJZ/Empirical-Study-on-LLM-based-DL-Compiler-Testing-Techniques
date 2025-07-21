'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.movedim\ntorch.Tensor.movedim(_input_tensor, source, destination)\n'
import torch
input_tensor = torch.rand(3, 4, 5)
print('Input tensor: ', input_tensor)
print('Dimension 0 to 2: ', input_tensor.movedim(0, 2))
print('Dimension 0 to 1: ', input_tensor.movedim(0, 1))
print('Dimension 1 to 2: ', input_tensor.movedim(1, 2))
print('Dimension 1 to 0: ', input_tensor.movedim(1, 0))
print('Dimension 2 to 0: ', input_tensor.movedim(2, 0))
print('Dimension 2 to 1: ', input_tensor.movedim(2, 1))