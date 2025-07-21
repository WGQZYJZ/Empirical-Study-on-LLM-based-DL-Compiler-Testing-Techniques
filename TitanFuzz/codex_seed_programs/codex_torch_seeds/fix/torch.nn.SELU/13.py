'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]]))
import torch
input_data = Variable(torch.Tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]]))
selu_activation_function = torch.nn.SELU()
output = selu_activation_function(input_data)
print(output)