'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
data = torch.randn(2, 2)
print(data)
relu = torch.nn.ReLU()
print(relu(data))