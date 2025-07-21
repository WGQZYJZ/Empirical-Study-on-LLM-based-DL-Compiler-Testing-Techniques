'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(torch.isfinite(input_tensor))