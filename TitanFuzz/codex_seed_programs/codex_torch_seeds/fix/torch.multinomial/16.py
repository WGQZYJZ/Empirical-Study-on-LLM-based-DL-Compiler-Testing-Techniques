'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multinomial\ntorch.multinomial(input, num_samples, replacement=False, *, generator=None, out=None)\n'
import torch
weights = torch.tensor([0.2, 0.8])
print('Input data:', weights)
out = torch.multinomial(weights, 1)
print('Output data:', out)