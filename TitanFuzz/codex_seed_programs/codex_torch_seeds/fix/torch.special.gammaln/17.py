'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.gammaln\ntorch.special.gammaln(input, *, out=None)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4, 5])
output = torch.special.gammaln(input_data)
print('Output: ', output)