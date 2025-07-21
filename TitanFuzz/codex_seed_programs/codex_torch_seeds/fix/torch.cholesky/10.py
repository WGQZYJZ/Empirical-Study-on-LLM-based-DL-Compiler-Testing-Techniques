'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky\ntorch.cholesky(input, upper=False, *, out=None)\n'
import torch
input = torch.randn(3, 3)
input = (input @ input.t())
output = torch.cholesky(input)
print('output: ', output)
print('output.t() @ output: ', (output.t() @ output))