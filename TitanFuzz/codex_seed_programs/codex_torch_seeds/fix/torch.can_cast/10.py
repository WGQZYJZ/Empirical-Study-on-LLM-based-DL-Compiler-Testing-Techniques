'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.can_cast\ntorch.can_cast(from, to)\n'
import torch
input_data = torch.randn(2, 3, 5)
print(torch.can_cast(torch.float32, torch.float64))
print(torch.can_cast(torch.float32, torch.float16))
print(torch.can_cast(torch.float32, torch.int8))
print(torch.can_cast(torch.float32, torch.int32))
print(torch.can_cast(torch.float32, torch.int64))