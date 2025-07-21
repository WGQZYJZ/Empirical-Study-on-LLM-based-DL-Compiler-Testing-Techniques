'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x_rot90 = torch.rot90(x, 1, dims=(0, 1))
print(x_rot90)