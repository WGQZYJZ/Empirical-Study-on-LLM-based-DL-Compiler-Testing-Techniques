'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Rprop\ntorch.optim.Rprop(params, lr=0.01, etas=(0.5, 1.2), step_sizes=(1e-06, 50))\n'
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
output_data = Variable(torch.randn(5, 2))
model = nn.Linear(3, 2)
optimizer = optim.Rprop(model.parameters(), lr=0.01, etas=(0.5, 1.2), step_sizes=(1e-06, 50))
for i in range(10):
    optimizer.zero_grad()
    output = model(input_data)
    loss = nn.MSELoss()(output, output_data)
    loss.backward()
    optimizer.step()
    print(loss)