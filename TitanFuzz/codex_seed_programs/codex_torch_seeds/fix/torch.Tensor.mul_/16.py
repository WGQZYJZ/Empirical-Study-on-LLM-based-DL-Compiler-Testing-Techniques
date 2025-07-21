'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul_\ntorch.Tensor.mul_(_input_tensor, value)\n'
import torch
input_tensor = torch.randn((1, 3, 3))
torch.Tensor.mul_(input_tensor, 2)
print(input_tensor)
'\nOutput:\ntensor([[[ 2.0384,  0.5145,  2.1448],\n         [-3.8704,  1.4388,  0.4172],\n         [ 1.4198,  2.8085,  1.5874]]])\n'