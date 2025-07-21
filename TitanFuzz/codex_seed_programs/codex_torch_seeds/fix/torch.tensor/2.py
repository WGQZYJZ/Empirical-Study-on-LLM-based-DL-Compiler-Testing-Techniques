'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor\ntorch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
data = [[1, 2], [3, 4]]
tensor_data = torch.tensor(data, dtype=torch.float32, device=torch.device('cpu'), requires_grad=True)
print(tensor_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randn\ntorch.randn(*size, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
tensor_data = torch.randn(2, 3, dtype=torch.float32, device=torch.device('cpu'), requires_grad=True)
print(tensor_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand\ntorch.rand(*size, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
tensor_data