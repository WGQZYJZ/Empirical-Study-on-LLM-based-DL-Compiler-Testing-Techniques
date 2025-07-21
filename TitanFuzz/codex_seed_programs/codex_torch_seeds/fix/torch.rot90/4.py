'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
a = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = torch.rot90(a, 1, [0, 1])
print(b)
b = torch.rot90(a, 2, [0, 1])
print(b)
b = torch.rot90(a, 3, [0, 1])
print(b)