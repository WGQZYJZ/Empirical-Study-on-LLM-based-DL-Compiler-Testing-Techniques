'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_exp\ntorch.matrix_exp(input)\n'
import torch
import math
input = torch.randn(2, 2)
output = torch.matrix_exp(input)
print(output)
expect = torch.tensor([[math.exp(input[0][0]), math.exp(input[0][1])], [math.exp(input[1][0]), math.exp(input[1][1])]])
print(expect)
print((output - expect))