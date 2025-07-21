'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.neg\ntorch.neg(input, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_data = torch.neg(input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)