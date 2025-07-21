'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.seed\ntorch.random.seed()\n'
import torch
input_data = torch.rand(1, 2)
torch.random.seed()
print(input_data)
print(torch.rand(1, 2))