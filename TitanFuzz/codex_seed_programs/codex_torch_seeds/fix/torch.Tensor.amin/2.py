'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amin\ntorch.Tensor.amin(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor)
torch.Tensor.amin(input_tensor, dim=None, keepdim=False)
torch.Tensor.amin(input_tensor, dim=0, keepdim=False)
torch.Tensor.amin(input_tensor, dim=1, keepdim=False)
torch.Tensor.amin(input_tensor, dim=None, keepdim=True)
torch.Tensor.amin(input_tensor, dim=0, keepdim=True)
torch.Tensor