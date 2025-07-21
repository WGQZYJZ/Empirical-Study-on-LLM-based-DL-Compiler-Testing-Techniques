'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cartesian_prod\ntorch.cartesian_prod(*tensors)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([6, 7, 8, 9, 10])
z = torch.tensor([11, 12, 13, 14, 15])
x_y_z = torch.cartesian_prod(x, y, z)
print(x_y_z)