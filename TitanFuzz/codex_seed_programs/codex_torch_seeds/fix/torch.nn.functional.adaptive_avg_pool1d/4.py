'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool1d\ntorch.nn.functional.adaptive_avg_pool1d(input, output_size)\n'
import torch
from torch.autograd import Variable
import numpy as np
input_data = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]])
input_data = Variable(torch.Tensor(input_data))
input_data = input_data.unsqueeze(0)
output = torch.nn.functional.adaptive_avg_pool1d(input_data, 2)
print(output)