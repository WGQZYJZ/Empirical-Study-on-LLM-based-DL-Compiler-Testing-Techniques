'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor\ntorch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
import torch
data = [[1, 2], [3, 4]]
torch_tensor = torch.tensor(data)
print(torch_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor\ntorch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
import torch
data = [[1, 2], [3, 4]]
torch_tensor = torch.tensor(data, dtype=torch.float32)
print(torch_tensor)