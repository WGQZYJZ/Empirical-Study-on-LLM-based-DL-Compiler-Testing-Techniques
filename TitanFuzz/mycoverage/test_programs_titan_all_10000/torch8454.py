import torch
from torch import nn
from torch.autograd import Variable
elements = torch.tensor([1, 2, 3, 4, 5])
test_elements = torch.tensor([1, 2, 3, 4, 5])
torch.isin(elements, test_elements)