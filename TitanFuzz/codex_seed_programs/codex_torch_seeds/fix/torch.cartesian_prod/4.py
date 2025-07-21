'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cartesian_prod\ntorch.cartesian_prod(*tensors)\n'
import torch
input1 = torch.tensor([1, 2, 3, 4])
input2 = torch.tensor([5, 6, 7, 8])
print(torch.cartesian_prod(input1, input2))