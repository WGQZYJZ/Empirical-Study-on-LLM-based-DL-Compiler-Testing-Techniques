'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sign\ntorch.sign(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1), (- 2), (- 3), (- 4), (- 5), (- 6), (- 7), (- 8), (- 9)])
y = torch.sign(x)
print(y)