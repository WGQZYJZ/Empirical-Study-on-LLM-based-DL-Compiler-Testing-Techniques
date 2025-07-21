'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.as_tensor\ntorch.as_tensor(data, dtype=None, device=None)\n'
import torch
data = [[1, 2], [3, 4]]
tensor = torch.as_tensor(data)
print(tensor)
data = [[1, 2], [3, 4]]
tensor = torch.as_tensor(data, dtype=torch.float32)
print(tensor)
data = [[1, 2], [3, 4]]
tensor = torch.as_tensor(data, dtype=torch.float32, device=torch.device('cuda'))
print(tensor)
data = [[1, 2], [3, 4]]
tensor = torch.as_tensor(data, dtype=torch.float32, device=torch.device('cpu'))
print(tensor)