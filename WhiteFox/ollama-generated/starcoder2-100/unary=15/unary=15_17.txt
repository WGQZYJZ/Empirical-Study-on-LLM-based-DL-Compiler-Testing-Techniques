

import torch
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)

        return v2

m  = Model()


inputs_to_the_model  = torch.randn(1, 3, 64, 64)
output  = m(inputs_to_the_model)


