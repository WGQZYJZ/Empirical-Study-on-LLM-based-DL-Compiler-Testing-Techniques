'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.repeat_interleave\ntorch.repeat_interleave(input, repeats, dim=None)\n'
import torch
input = torch.arange(4, dtype=torch.float32).reshape(2, 2)
print(input)
repeats = torch.tensor([2, 3])
print(repeats)
output = torch.repeat_interleave(input, repeats, dim=0)
print(output)
output = torch.repeat_interleave(input, repeats, dim=1)
print(output)