'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad2d\ntorch.nn.ReflectionPad2d(padding)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 3, 3))
reflectionPad2d = torch.nn.ReflectionPad2d(padding=1)
output = reflectionPad2d(input)
print(output)