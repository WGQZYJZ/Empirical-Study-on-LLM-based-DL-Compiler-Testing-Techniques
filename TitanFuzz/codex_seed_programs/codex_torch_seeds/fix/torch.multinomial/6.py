'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multinomial\ntorch.multinomial(input, num_samples, replacement=False, *, generator=None, out=None)\n'
import torch
input = torch.Tensor([[0.2, 0.3, 0.5]])
output = torch.multinomial(input, 3, replacement=False)
print(output)
output = torch.multinomial(input, 3, replacement=True)
print(output)