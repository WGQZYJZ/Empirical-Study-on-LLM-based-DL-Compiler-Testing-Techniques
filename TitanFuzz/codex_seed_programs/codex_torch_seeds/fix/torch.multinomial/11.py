'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multinomial\ntorch.multinomial(input, num_samples, replacement=False, *, generator=None, out=None)\n'
import torch
input = torch.Tensor([[0.3, 0.2, 0.5], [0.1, 0.2, 0.7]])
output = torch.multinomial(input, 2, replacement=False)
print(output)
output = torch.multinomial(input, 2, replacement=True)
print(output)