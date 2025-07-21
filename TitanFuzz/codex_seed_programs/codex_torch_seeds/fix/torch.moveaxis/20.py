'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
tensor = torch.randn(2, 3, 4)
print('tensor: ', tensor)
print('tensor.shape: ', tensor.shape)
tensor = torch.moveaxis(tensor, 0, (- 1))
print('tensor.shape: ', tensor.shape)
print('tensor: ', tensor)