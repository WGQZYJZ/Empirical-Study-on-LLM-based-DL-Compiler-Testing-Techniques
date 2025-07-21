'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg\ntorch.Tensor.neg(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 2, 3)
result = torch.Tensor.neg(input_tensor)
print(result)