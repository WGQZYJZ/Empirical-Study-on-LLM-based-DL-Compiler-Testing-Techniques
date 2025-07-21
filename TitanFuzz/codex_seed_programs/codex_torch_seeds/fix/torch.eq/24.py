'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eq\ntorch.eq(input, other, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
print(torch.eq(input_data, input_data))
print(torch.eq(input_data, torch.randn(2, 3)))
print(torch.eq(input_data, torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])))