'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu_\ntorch.nn.functional.rrelu_(input, lower=1./8, upper=1./3, training=False)\n'
import torch
input = torch.randn(4, 4)
print('Input is:\n', input)
output = torch.nn.functional.rrelu_(input)
print('Output is:\n', output)