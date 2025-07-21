'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor\ntorch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
input_data = [[1, 2, 3], [4, 5, 6]]
input_tensor = torch.tensor(input_data)
print(input_tensor)