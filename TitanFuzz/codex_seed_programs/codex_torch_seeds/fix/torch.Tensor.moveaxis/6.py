'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.moveaxis\ntorch.Tensor.moveaxis(_input_tensor, source, destination)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('input_tensor: ', input_tensor)
print('output_tensor: ', input_tensor.moveaxis(source=0, destination=2))
print('output_tensor: ', input_tensor.moveaxis(source=1, destination=0))
print('output_tensor: ', input_tensor.moveaxis(source=2, destination=0))
print('output_tensor: ', input_tensor.moveaxis(source=(0, 1), destination=(1, 0)))
print('output_tensor: ', input_tensor.moveaxis(source=(0, 2), destination=(2, 0)))