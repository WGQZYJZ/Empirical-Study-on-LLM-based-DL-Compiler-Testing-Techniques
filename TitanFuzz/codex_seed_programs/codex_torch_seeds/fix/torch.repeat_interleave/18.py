'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.repeat_interleave\ntorch.repeat_interleave(input, repeats, dim=None)\n'
import torch
import torch
x = torch.tensor([1, 2, 3, 4, 5])
print(x)
output = torch.repeat_interleave(x, repeats=3, dim=0)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.roll\ntorch.roll(input, shifts, dims)\n'
import torch
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x)
output = torch.roll(x, shifts=1, dims=1)
print(output)