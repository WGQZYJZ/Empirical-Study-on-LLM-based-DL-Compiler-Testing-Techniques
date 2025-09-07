import torch
from torch import nn
from torch.autograd import Variable
params = torch.tensor([1.0, 0.0], requires_grad=True)
optimizer = torch.optim.RMSprop([params], lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False)
optimizer.zero_grad()
loss = ((params[0] ** 2) + (params[1] ** 2))
loss.backward()
optimizer.step()