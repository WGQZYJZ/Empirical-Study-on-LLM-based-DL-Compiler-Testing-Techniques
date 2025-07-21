'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sequential\ntorch.nn.Sequential(*args)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
print(input_data)
seq = torch.nn.Sequential(torch.nn.Linear(3, 5), torch.nn.ReLU(), torch.nn.Linear(5, 2), torch.nn.ReLU())
print(seq)
output = seq.forward(input_data)
print(output)
for param in seq.parameters():
    print(param)