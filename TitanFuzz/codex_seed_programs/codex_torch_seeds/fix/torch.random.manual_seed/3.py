'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.manual_seed\ntorch.random.manual_seed(seed)\n'
import torch
input = torch.randn(3, 5, dtype=torch.float)
print(input)
torch.random.manual_seed(123)
input = torch.randn(3, 5, dtype=torch.float)
print(input)