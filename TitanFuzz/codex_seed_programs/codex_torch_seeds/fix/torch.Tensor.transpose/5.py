'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose\ntorch.Tensor.transpose(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.transpose(input_tensor, 0, 1)
print('Output tensor: ', output_tensor)
'\nOutput:\nInput tensor:  tensor([[ 0.5155, -0.4166,  0.8282],\n        [-0.5165,  0.5173, -0.5772]])\nOutput tensor:  tensor([[ 0.5155, -0.5165],\n        [-0.4166,  0.5173],\n        [ 0.8282, -0.5772]])\n'