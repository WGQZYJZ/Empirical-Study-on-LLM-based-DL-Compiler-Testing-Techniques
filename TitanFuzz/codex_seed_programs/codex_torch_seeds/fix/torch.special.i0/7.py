'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i0\ntorch.special.i0(input, *, out=None)\n'
import torch
input = torch.tensor([1, 2, 3, 4, 5])
print(torch.special.i0(input))
print(torch.special.i0(input, out=torch.FloatTensor()))
print(torch.special.i0(input, out=torch.DoubleTensor()))