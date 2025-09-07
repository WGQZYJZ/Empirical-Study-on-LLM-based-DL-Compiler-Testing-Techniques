import torch
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        splitted_tensor = torch.split(x1, 32)
        concatenated_tensor = torch.cat([splitted_tensor[i] for i in range(len(splitted_tensor))], dim=0)
        return concatenated_tensor
m = Model()


inputs = [torch.randn(4,8)]
__outputs__ = []
for i in inputs:
    __outputs__.append(m(i))



return True
