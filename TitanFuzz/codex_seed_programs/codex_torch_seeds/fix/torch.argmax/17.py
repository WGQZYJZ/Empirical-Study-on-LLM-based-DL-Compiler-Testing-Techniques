'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmax\ntorch.argmax(input, dim, keepdim=False)\n'
import torch
data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(data)
result = torch.argmax(data, dim=1)
print(result)