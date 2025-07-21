'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmax\ntorch.argmax(input, dim, keepdim=False)\n'
import torch
input = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
result = torch.argmax(input, dim=1)
print('result: ', result)