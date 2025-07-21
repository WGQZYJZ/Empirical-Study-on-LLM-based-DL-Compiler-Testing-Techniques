'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_not\ntorch.Tensor.logical_not(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
output_tensor = torch.Tensor.logical_not(input_tensor)
print('Input tensor:')
print(input_tensor)
print('Output tensor:')
print(output_tensor)
'\nExpected output:\nInput tensor:\ntensor([[1, 0, 1],\n        [0, 1, 0],\n        [1, 0, 1]])\nOutput tensor:\ntensor([[0, 1, 0],\n        [1, 0, 1],\n        [0, 1, 0]])\n'