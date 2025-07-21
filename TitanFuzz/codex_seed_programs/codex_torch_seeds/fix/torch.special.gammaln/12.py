'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.gammaln\ntorch.special.gammaln(input, *, out=None)\n'
import torch
input_data = torch.tensor([1.0, 2.0, 3.0])
print('input_data: ', input_data)
output_data = torch.special.gammaln(input_data)
print('output_data: ', output_data)