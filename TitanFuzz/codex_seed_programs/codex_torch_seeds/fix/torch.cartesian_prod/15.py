'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cartesian_prod\ntorch.cartesian_prod(*tensors)\n'
import torch
tensors = [torch.tensor([1, 2, 3]), torch.tensor([4, 5]), torch.tensor([6, 7])]
print(torch.cartesian_prod(*tensors))