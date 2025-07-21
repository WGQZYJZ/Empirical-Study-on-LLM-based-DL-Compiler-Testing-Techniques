'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.neg\ntorch.neg(input, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2], [3, 4]])
print('Input data: \n', input_data)
output = torch.neg(input_data)
print('Output: \n', output)