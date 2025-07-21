'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor\ntorch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
data = [[1, 2], [3, 4]]
tensor = torch.tensor(data)
print(tensor)
tensor = torch.tensor(data, dtype=torch.float32)
print(tensor)
tensor = torch.tensor(data, dtype=torch.float32, device=torch.device('cuda'))
print(tensor)
tensor = torch.tensor(data, dtype=torch.float32, device=torch.device('cuda'), requires_grad=True)
print(tensor)
tensor = torch.tensor(data, dtype=torch.float32, device=torch.device('cuda'), requires_grad=True, pin_memory=True)