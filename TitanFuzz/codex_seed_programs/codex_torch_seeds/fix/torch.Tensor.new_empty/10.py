'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_empty\ntorch.Tensor.new_empty(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = torch.randn(1, 2, 3, 4)
out_tensor = torch.Tensor.new_empty(_input_tensor, size=(2, 3, 4, 5), dtype=torch.float, device=torch.device('cuda'), requires_grad=True)
print(out_tensor)