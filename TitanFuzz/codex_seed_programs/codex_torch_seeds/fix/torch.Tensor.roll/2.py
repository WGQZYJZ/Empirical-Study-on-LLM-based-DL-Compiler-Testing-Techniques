'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.roll\ntorch.Tensor.roll(_input_tensor, shifts, dims)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('Input tensor: \n', input_tensor)
shifts = torch.tensor([1, 2])
result = torch.Tensor.roll(input_tensor, shifts, dims=0)
print('\nResult: \n', result)