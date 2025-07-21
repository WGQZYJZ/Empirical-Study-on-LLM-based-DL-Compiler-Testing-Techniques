'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.stack\ntorch.stack(tensors, dim=0, *, out=None)\n'
import torch
input_1 = torch.rand(3, 4)
input_2 = torch.rand(3, 4)
input_3 = torch.rand(3, 4)
output = torch.stack([input_1, input_2, input_3])
print(output)