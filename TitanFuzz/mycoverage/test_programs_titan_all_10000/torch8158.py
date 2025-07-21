import torch
from torch import nn
from torch.autograd import Variable
input_dim = 2
output_dim = 1
x = torch.tensor([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0]], requires_grad=True)
y = torch.tensor([[2.0], [4.0], [6.0]], requires_grad=True)
model = torch.nn.Sequential(torch.nn.Linear(input_dim, output_dim))
loss_fn = torch.nn.MSELoss(reduction='sum')
learning_rate = 0.0001
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)