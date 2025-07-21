'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ge_\ntorch.Tensor.ge_(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3)
torch.Tensor.ge_(input_tensor, 0)
print(input_tensor)