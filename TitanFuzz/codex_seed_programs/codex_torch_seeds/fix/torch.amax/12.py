'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amax\ntorch.amax(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(input_data)
max_val_1 = torch.amax(input_data)
print(max_val_1)
max_val_2 = torch.amax(input_data, dim=1)
print(max_val_2)
max_val_3 = torch.amax(input_data, dim=1, keepdim=True)
print(max_val_3)