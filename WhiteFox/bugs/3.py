import torch
import torch.nn as nn

torch.manual_seed(420)

class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.fc1 = nn.Linear(3, 3)

    def forward(self, x):
        x = self.fc1(x.permute(1, 2, 0))
        return x
input = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

func = Model().to('cpu')

with torch.no_grad():
    jit_func = torch.compile(func)
    print(func(input))
    print(jit_func(input))
