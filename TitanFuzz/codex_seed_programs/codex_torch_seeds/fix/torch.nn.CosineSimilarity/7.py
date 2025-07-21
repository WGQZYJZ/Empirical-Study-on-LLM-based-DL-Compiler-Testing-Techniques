'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineSimilarity\ntorch.nn.CosineSimilarity(dim=1, eps=1e-08)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
from torch.autograd import Variable
import numpy as np
input_data = Variable(torch.randn(3, 5))
print(input_data)
cos = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
output = cos(input_data, input_data)
print(output)
print(output)
print(output.size())