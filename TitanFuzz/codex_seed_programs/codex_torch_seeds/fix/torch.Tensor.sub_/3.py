'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub_\ntorch.Tensor.sub_(_input_tensor, other, *, alpha=1)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
other = torch.tensor([[1, 1], [1, 1]], dtype=torch.float32)
torch.Tensor.sub_(input_tensor, other, alpha=1)
print(input_tensor)