'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.can_cast\ntorch.can_cast(from, to)\n'
import torch
data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(data)
print(torch.can_cast(torch.float32, torch.float64))
print(torch.can_cast(torch.float64, torch.float32))
print(torch.can_cast(torch.float64, torch.int32))
print(torch.can_cast(torch.int32, torch.float64))
print(torch.can_cast(torch.int32, torch.float32))
print(torch.can_cast(torch.float32, torch.int32))