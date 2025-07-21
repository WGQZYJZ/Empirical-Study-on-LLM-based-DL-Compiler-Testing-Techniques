'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PReLU\ntorch.nn.PReLU(num_parameters=1, init=0.25, device=None, dtype=None)\n'
import torch
import torch.nn as nn
x_input = torch.rand(5, 3)
print(x_input)
prelu = nn.PReLU()
print(prelu)
y_output = prelu(x_input)
print(y_output)
y_output2 = prelu(y_output)
print(y_output2)
y_output3 = prelu(y_output2)
print(y_output3)
y_output4 = prelu(y_output3)
print(y_output4)
y_output5 = prelu(y_output4)
print(y_output5)
y_output6 = prelu(y_output5)