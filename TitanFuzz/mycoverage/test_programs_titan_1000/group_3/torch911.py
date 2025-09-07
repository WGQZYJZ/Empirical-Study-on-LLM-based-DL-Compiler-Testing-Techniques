import torch
from torch import nn
from torch.autograd import Variable
if True:
    import torch
    import torch.nn as nn
    input_tensor = torch.rand(2, 3, 4, 5)
    conv_layer = nn.Conv2d(3, 4, 2)
    conv_layer.weight.data = torch.ones(4, 3, 2, 2)
    conv_layer.bias.data = torch.ones(4)
    parameters = [conv_layer.weight, conv_layer.bias]
    vector = torch.nn.utils.parameters_to_vector(parameters)
    print(vector)