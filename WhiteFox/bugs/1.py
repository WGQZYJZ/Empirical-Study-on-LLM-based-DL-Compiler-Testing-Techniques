import torch
import torch.nn as nn

torch.manual_seed(420)

class Model(torch.nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.linear = torch.nn.functional.linear
        self.linear_weight = torch.randn(4, 4).cuda()
        self.bias = torch.randn(1, 4).cuda()

    def forward(self, x):
        x = self.linear(x, self.linear_weight, self.bias)
        return x

input = torch.randn(1, 3, 4).cuda()

func = Model().cuda()

res1 = func(input)
print(res1)

jit_func = torch.compile(func)
res2 = jit_func(input)
