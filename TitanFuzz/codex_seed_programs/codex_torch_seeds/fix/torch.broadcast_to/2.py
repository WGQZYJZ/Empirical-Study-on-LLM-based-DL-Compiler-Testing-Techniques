'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_to\ntorch.broadcast_to(input, shape)\n'
import torch
input = torch.rand(2, 3, 4)
print('Input:', input)
output = torch.broadcast_to(input, (4, 2, 3, 4))
print('Output:', output)
'\nTask 4: Call the API torch.broadcast_tensors\ntorch.broadcast_tensors(*tensors)\n'
input1 = torch.rand(2, 3, 4)
input2 = torch.rand(3, 4)
print('Input1:', input1)
print('Input2:', input2)
output = torch.broadcast_tensors(input1, input2)
print('Output:', output)