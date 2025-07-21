'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randperm\ntorch.randperm(n, *, generator=None, out=None, dtype=torch.int64, layout=torch.strided, device=None, requires_grad=False, pin_memory=False)\n'
import torch
input_data = torch.randperm(10)
print(input_data)
input_data = torch.randperm(10, dtype=torch.float32)
print(input_data)
input_data = torch.randperm(10, dtype=torch.float32, device=torch.device('cuda'))
print(input_data)
input_data = torch.randperm(10, dtype=torch.float32, device=torch.device('cuda'), requires_grad=True)
print(input_data)