'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcdiv_\ntorch.Tensor.addcdiv_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
input_tensor = torch.randn(3, 3)
tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
input_tensor.addcdiv_(tensor1, tensor2)
print(input_tensor)