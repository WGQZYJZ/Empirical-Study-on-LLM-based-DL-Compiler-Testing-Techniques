'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummax\ntorch.cummax(input, dim, *, out=None)\n'
import torch
if True:
    input = torch.randn(3, 3)
    print('Input data:')
    print(input)
    print('Result of torch.cummax:')
    print(torch.cummax(input, dim=0))
    print(torch.cummax(input, dim=1))