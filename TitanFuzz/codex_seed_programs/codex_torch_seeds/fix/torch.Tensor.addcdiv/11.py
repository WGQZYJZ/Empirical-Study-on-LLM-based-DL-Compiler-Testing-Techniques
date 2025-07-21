'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcdiv\ntorch.Tensor.addcdiv(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
input_tensor = torch.randn(4, 4)
tensor1 = torch.randn(4, 4)
tensor2 = torch.randn(4, 4)
output_tensor = torch.Tensor.addcdiv(input_tensor, tensor1, tensor2)
print('output_tensor = ', output_tensor)