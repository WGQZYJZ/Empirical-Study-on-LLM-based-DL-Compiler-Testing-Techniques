'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eq\ntorch.eq(input, other, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
other_data = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(torch.__version__)
print(input_data)
print(other_data)
print(torch.eq(input_data, other_data))