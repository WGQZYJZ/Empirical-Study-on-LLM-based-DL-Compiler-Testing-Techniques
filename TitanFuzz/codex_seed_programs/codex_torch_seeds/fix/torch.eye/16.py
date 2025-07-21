'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eye\ntorch.eye(n, m=None, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
eye_data = torch.eye(3)
print(eye_data)
mm_data = torch.mm(input_data, eye_data)
print(mm_data)