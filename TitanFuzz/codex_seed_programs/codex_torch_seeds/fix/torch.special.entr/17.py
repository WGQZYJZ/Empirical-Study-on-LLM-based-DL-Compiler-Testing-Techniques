'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.entr\ntorch.special.entr(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('Input data: ', input)
entr = torch.special.entr(input)
print('Entropy of input data: ', entr)