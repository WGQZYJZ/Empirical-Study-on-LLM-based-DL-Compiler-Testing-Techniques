'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.manual_seed\ntorch.random.manual_seed(seed)\n'
import torch
input = torch.randn(1, 1, 3, 3)
torch.random.manual_seed(2)
print(torch.randn(1, 1, 3, 3))