import torch
import torch.nn as nn

torch.manual_seed(420)

class MyModel(torch.nn.Module):

    def forward(self, x):
        x = x * 2
        x = torch.nn.functional.dropout(x, p=0.5)
        x = torch.relu(x)
        return x
x = torch.tensor([[1, 2, 3], [4, 5, 6]])

func = MyModel()
jit_func = torch.compile(func)

print(func(x))
print(jit_func(x))

