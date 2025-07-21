'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Threshold\ntorch.nn.Threshold(threshold, value, inplace=False)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[(- 0.5), (- 0.5), 0.5, 0.5]]))
print(input_data)
threshold = 0.1
threshold_layer = torch.nn.Threshold(threshold, 0)
output = threshold_layer(input_data)
print(output)