import torch
from torch import nn
from torch.autograd import Variable
if True:
    elements = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test_elements = torch.tensor([2, 4, 6, 8])
    result = torch.isin(elements, test_elements)
    print('result = ', result)