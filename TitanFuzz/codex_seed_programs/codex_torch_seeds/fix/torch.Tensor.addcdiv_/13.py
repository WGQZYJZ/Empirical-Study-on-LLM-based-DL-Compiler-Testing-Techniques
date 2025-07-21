'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcdiv_\ntorch.Tensor.addcdiv_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
input_tensor = torch.rand(10, 10)
tensor1 = torch.rand(10, 10)
tensor2 = torch.rand(10, 10)
input_tensor.addcdiv_(tensor1, tensor2)
print(input_tensor)