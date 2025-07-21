'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.seed\ntorch.seed()\n'
import torch
input_data = torch.rand(1, 1, 2, 2)
print(input_data)
torch.seed()