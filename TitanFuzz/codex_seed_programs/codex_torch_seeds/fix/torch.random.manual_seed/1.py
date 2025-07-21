'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.manual_seed\ntorch.random.manual_seed(seed)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
torch.random.manual_seed(123)
print(torch.randn(2, 3))