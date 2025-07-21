'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.gammaincc\ntorch.special.gammaincc(input, other, *, out=None)\n'
import torch
input1 = torch.randn(4, 4)
input2 = torch.randn(4, 4)
torch.special.gammaincc(input1, input2, out=None)