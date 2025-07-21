'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isreal\ntorch.isreal(input)\n'
import torch
input_data = torch.randn(1, 2, 3, 4)
print(input_data)
print(torch.isreal(input_data))