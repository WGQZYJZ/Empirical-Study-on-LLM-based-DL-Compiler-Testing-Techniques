'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nan_to_num\ntorch.nan_to_num(input, nan=0.0, posinf=None, neginf=None, *, out=None)\n'
import torch
input = torch.tensor([[float('nan'), float('inf'), float('-inf')], [1, 2, 3], [0, 0, 0]])
output = torch.nan_to_num(input, 0.0, None, None)
print(output)
'\nOUTPUT:\ntensor([[0., 0., 0.],\n        [1., 2., 3.],\n        [0., 0., 0.]])\n'