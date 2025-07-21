'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multinomial\ntorch.multinomial(input, num_samples, replacement=False, *, generator=None, out=None)\n'
import torch
input_data = torch.tensor([[0.2, 0.4, 0.4]])
output = torch.multinomial(input_data, 2)
print(output)