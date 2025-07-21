import torch
from torch import nn
from torch.autograd import Variable
if True:
    import torch
    input_tensor = torch.rand(3, 3)
    other_tensor = torch.rand(3, 3)
    result = torch.Tensor.minimum(input_tensor, other_tensor)
    print('The result is: ', result)