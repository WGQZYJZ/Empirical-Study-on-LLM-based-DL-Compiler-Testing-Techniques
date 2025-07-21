'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multinomial\ntorch.multinomial(input, num_samples, replacement=False, *, generator=None, out=None)\n'
import torch
import torch
input = torch.tensor([[10.0, 10.0, 10.0, 10.0, 10.0], [1.0, 2.0, 3.0, 4.0, 5.0]])
output = torch.multinomial(input, 3)
print(output)