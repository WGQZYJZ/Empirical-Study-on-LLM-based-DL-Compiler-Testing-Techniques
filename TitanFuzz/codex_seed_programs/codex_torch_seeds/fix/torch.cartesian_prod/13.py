'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cartesian_prod\ntorch.cartesian_prod(*tensors)\n'
import torch
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5])
c = torch.tensor([6, 7, 8])
print(torch.cartesian_prod(a, b, c))
'\nTask 4: Call the API torch.combinations\ntorch.combinations(tensor, r)\n'
print(torch.combinations(a, 2))