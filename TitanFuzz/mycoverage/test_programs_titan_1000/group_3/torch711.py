import torch
from torch import nn
from torch.autograd import Variable
elements = torch.randint(0, 10, (2, 3))
test_elements = torch.randint(0, 10, (2, 3))
isin_result = torch.isin(elements, test_elements)