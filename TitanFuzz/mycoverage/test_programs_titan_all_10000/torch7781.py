import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
optimizer = torch.optim.Adamax([input_data], lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
optimizer.step()
optimizer.step()