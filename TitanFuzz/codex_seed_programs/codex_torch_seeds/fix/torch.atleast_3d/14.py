'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_3d\ntorch.atleast_3d(*tensors)\n'
import torch
input_1 = torch.randn(2, 3)
input_2 = torch.randn(2, 3, 4)
output = torch.atleast_3d(input_1, input_2)
print(output)