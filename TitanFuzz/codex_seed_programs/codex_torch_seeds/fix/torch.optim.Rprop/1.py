'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Rprop\ntorch.optim.Rprop(params, lr=0.01, etas=(0.5, 1.2), step_sizes=(1e-06, 50))\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
from torch.optim import Rprop
batch_size = 128
input_size = 1000
hidden_size = 100
output_size = 10
x = Variable(torch.randn(batch_size, input_size), requires_grad=False)
y = Variable(torch.randn(batch_size, output_size), requires_grad=False)
model = torch.nn.Sequential(torch.nn.Linear(input_size, hidden_size), torch.nn.ReLU(), torch.nn.Linear(hidden_size, output_size))
loss_fn = torch.nn.MSELoss(size_average=False)
learning_rate = 0.01
optimizer = Rprop(model.parameters(), lr=learning_rate)
for t in range(500):
    y_pred = model(x)