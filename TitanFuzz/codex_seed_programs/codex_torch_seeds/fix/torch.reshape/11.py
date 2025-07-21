'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reshape\ntorch.reshape(input, shape)\n'
import torch
input = torch.randn(2, 3, 4)
print(input)
print(torch.reshape(input, (3, 8)))
print(torch.reshape(input, (3, (- 1))))
print(torch.reshape(input, ((- 1), 8)))
print(torch.reshape(input, ((- 1),)))