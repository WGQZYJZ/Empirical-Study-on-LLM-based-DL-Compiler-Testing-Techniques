'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cartesian_prod\ntorch.cartesian_prod(*tensors)\n'
import torch
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
torch.cartesian_prod(a, b)
'\ntensor([[1, 4],\n        [1, 5],\n        [1, 6],\n        [2, 4],\n        [2, 5],\n        [2, 6],\n        [3, 4],\n        [3, 5],\n        [3, 6]])\n'
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
c = torch.tensor([7, 8, 9])
torch.cartesian_prod(a, b, c)