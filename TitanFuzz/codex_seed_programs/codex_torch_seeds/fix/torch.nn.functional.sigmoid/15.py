'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.sigmoid\ntorch.nn.functional.sigmoid(input)\n'
import torch
input_data = torch.tensor([[0.1, 0.2, 0.3, 0.4]])
print(torch.nn.functional.sigmoid(input_data))