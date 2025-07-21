'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor\ntorch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
data = [[1, 2], [3, 4]]
tensor_data = torch.tensor(data)
print(tensor_data)
tensor_data = torch.tensor(data, dtype=torch.float32)
print(tensor_data)
tensor_data = torch.tensor(data, dtype=torch.float32, requires_grad=True)
print(tensor_data)