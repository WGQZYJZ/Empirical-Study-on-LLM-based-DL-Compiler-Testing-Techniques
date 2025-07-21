'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multinomial\ntorch.multinomial(input, num_samples, replacement=False, *, generator=None, out=None)\n'
import torch
input = torch.FloatTensor([[0.1, 0.2, 0.3, 0.4, 0.5], [0.1, 0.2, 0.3, 0.4, 0.5]])
result = torch.multinomial(input, 3, replacement=False)
print(result)
result = torch.multinomial(input, 3, replacement=True)
print(result)
result = torch.multinomial(input, 3, replacement=True, out=torch.LongTensor([0, 0, 0]))
print(result)