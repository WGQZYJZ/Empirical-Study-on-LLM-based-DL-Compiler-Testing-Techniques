'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cartesian_prod\ntorch.cartesian_prod(*tensors)\n'
import torch
tensors = []
tensors.append(torch.tensor([1, 2, 3]))
tensors.append(torch.tensor([4, 5, 6]))
tensors.append(torch.tensor([7, 8, 9]))
print('torch.cartesian_prod(*tensors) = ', torch.cartesian_prod(*tensors))