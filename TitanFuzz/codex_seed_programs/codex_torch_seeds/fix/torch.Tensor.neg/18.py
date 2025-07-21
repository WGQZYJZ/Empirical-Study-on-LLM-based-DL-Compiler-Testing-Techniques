'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg\ntorch.Tensor.neg(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print(input_tensor)
neg_tensor = torch.Tensor.neg(input_tensor)
print(neg_tensor)