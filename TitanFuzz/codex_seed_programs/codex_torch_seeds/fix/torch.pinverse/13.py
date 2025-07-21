'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pinverse\ntorch.pinverse(input, rcond=1e-15)\n'
import torch
input = torch.Tensor([[1, 2, 3], [4, 5, 6]])
output = torch.pinverse(input, rcond=1e-15)
print(output)