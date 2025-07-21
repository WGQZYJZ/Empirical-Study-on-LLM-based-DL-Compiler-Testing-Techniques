'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.feature_alpha_dropout\ntorch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
input_data = torch.randn(3, 4)
print(input_data)
output_data = torch.nn.functional.feature_alpha_dropout(input_data, p=0.5, training=False, inplace=False)
print(output_data)