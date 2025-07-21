'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multinomial\ntorch.multinomial(input, num_samples, replacement=False, *, generator=None, out=None)\n'
import torch
input = torch.Tensor([[0.1, 0.2, 0.3, 0.4]])
torch.multinomial(input, 2)
'\nTask 4: Call the API torch.multinomial\ntorch.multinomial(input, num_samples, replacement=False, *, generator=None, out=None)\n'
torch.multinomial(input, 3, replacement=True)