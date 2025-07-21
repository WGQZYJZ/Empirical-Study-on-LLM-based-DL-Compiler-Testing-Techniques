'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multinomial\ntorch.multinomial(input, num_samples, replacement=False, *, generator=None, out=None)\n'
import torch
input = torch.Tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
output = torch.multinomial(input, 3, replacement=False)
print(output)