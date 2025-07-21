'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.det\ntorch.det(input)\n'
import torch
x = torch.tensor([[2, 3], [1, 2]], dtype=torch.float)
print(torch.det(x))