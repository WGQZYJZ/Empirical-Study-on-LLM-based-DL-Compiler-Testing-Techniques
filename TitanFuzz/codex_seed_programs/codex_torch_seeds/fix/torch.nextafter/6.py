'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nextafter\ntorch.nextafter(input, other, *, out=None)\n'
import torch
input = torch.tensor([1.0, 2.0, 3.0])
other = torch.tensor([3.0, 2.0, 1.0])
torch.nextafter(input, other)
torch.nextafter(input, other, out=input)
print(input)