'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
data = torch.randn(2, 3)
print(data)
print(torch.rot90(data, 1, [0, 1]))
print(torch.rot90(data, 2, [0, 1]))
print(torch.rot90(data, 3, [0, 1]))
print(torch.rot90(data, 4, [0, 1]))
print(torch.rot90(data, 5, [0, 1]))
print(torch.rot90(data, 6, [0, 1]))
print(torch.rot90(data, 7, [0, 1]))
print(torch.rot90(data, 8, [0, 1]))
print(torch.rot90(data, 9, [0, 1]))