'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_tensor\ntorch.Tensor.new_tensor(_input_tensor, data, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = torch.rand(2, 3)
data = torch.rand(2, 3)
torch.Tensor.new_tensor(_input_tensor, data)
torch.Tensor.new_tensor(_input_tensor, data, dtype=torch.int64)
torch.Tensor.new_tensor(_input_tensor, data, device=torch.device('cpu'))
torch.Tensor.new_tensor(_input_tensor, data, requires_grad=True)
torch.Tensor.new_tensor(_input_tensor, data, dtype=torch.int64, device=torch.device('cpu'), requires_grad=True)