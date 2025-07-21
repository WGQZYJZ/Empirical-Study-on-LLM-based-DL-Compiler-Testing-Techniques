'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.positive\ntorch.positive(input)\n'
import torch
data = torch.randn(5, 3)
result = torch.positive(data)
print(result)