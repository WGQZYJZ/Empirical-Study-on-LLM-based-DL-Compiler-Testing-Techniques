'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.local_response_norm\ntorch.nn.functional.local_response_norm(input, size, alpha=0.0001, beta=0.75, k=1.0)\n'
import torch
from torch.autograd import Variable
import torch
input_data = torch.randn(1, 1, 3, 3)
print(input_data)
output = torch.nn.functional.local_response_norm(input_data, 1)
print(output)