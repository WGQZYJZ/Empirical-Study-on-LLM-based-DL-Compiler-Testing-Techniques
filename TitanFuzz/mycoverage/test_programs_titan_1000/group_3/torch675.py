import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 3)
y = torch.randn(3, 3)
z = torch.randn(3, 3)
x_annotated = torch.jit.annotate(torch.Tensor, x)
y_annotated = torch.jit.annotate(torch.Tensor, y)
z_annotated = torch.jit.annotate(torch.Tensor, z)
x_annotated = (x_annotated + y_annotated)
y_annotated = (y_annotated + z_annotated)
x_annotated = (x_annotated + y_annotated)
y_annotated = (y_annotated + z_annotated)