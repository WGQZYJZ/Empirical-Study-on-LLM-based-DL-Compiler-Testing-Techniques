'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fliplr\ntorch.Tensor.fliplr(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor:')
print(input_tensor)
print('\nOutput tensor:')
print(torch.Tensor.fliplr(input_tensor))
print('\nOutput tensor:')
print(torch.fliplr(input_tensor))