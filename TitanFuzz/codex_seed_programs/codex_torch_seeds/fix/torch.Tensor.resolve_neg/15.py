'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resolve_neg\ntorch.Tensor.resolve_neg(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print(input_tensor)
torch.Tensor.resolve_neg(input_tensor)
print(input_tensor)