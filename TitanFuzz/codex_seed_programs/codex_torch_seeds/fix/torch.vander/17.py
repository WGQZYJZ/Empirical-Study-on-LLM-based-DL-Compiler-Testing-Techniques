'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vander\ntorch.vander(x, N=None, increasing=False)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4, 5])
print(torch.vander(input_data))