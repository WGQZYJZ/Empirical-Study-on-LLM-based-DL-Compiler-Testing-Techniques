'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 3, 5, 5, 5))
print(input_data)
output = torch.nn.AdaptiveAvgPool3d(output_size=(1, 1, 1))(input_data)
print(output)