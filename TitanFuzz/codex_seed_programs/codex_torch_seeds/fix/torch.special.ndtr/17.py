'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.ndtr\ntorch.special.ndtr(input, *, out=None)\n'
import torch
input = torch.tensor([(- 1.0), 0.0, 1.0])
output = torch.special.ndtr(input)
print('The result of torch.special.ndtr(input) is:', output)