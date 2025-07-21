'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.local_response_norm\ntorch.nn.functional.local_response_norm(input, size, alpha=0.0001, beta=0.75, k=1.0)\n'
import torch
from torch.autograd import Variable
from torch.nn import functional as F
import torch
input = torch.randn(1, 5, 5, 5)
output = F.local_response_norm(input, size=3, alpha=0.0001, beta=0.75, k=1.0)
print(output)