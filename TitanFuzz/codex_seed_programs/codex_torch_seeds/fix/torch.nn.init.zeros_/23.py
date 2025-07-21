'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.zeros_\ntorch.nn.init.zeros_(tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.nn.init.zeros_(input_tensor)
print(input_tensor)