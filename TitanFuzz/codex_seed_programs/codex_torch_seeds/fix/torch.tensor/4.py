'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor\ntorch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
data = [[1, 2, 3], [4, 5, 6]]
tensor = torch.tensor(data)
print(tensor)
data = [[1, 2, 3], [4, 5, 6]]
tensor = torch.tensor(data, dtype=torch.float32)
print(tensor)
data = [[1, 2, 3], [4, 5, 6]]
tensor = torch.tensor(data, dtype=torch.float32, device=torch.device('cuda'))
print(tensor)
data = [[1, 2, 3], [4, 5, 6]]
tensor = torch.tensor(data, dtype=torch.float32, device=torch.device('cpu'))
print(tensor)
data = [[1, 2, 3], [4, 5, 6]]
tensor = torch.tensor(data, dtype=torch.float32, device=torch.device('cuda:0'))
print(tensor)
data