'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multinomial\ntorch.multinomial(input, num_samples, replacement=False, *, generator=None, out=None)\n'
import torch
data = torch.tensor([0.1, 0.2, 0.3, 0.4])
print(torch.multinomial(data, 2))
print(torch.multinomial(data, 3))