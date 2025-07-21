import torch
from torch import nn
from torch.autograd import Variable
batch_size = 2
input_size = 3
hidden_size = 2
input_tensor = torch.randn(batch_size, input_size)
hidden_tensor = torch.randn(batch_size, hidden_size)
weight_tensor = torch.randn(hidden_size, input_size)
batch_size = 2
input_size = 3
hidden_size = 2
input_tensor = torch.randn(batch_size, input_size)
hidden_tensor = torch.randn(batch_size, hidden_size)
weight_tensor = torch.randn(hidden_size, input_size)
torch.Tensor.addbmm_(input_tensor, hidden_tensor, weight_tensor, beta=1, alpha=1)