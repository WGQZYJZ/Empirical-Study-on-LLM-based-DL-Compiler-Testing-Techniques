'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GLU\ntorch.nn.GLU(dim=-1)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(2, 3, 4))
glu = torch.nn.GLU()
output = glu(input_data)
print(output)