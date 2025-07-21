'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.absolute\ntorch.absolute(input, *, out=None)\n'
import torch
input = torch.tensor([(- 1), (- 2), 3, 4], dtype=torch.float32)
print('Input data: ', input)
output = torch.absolute(input)
print('Output: ', output)