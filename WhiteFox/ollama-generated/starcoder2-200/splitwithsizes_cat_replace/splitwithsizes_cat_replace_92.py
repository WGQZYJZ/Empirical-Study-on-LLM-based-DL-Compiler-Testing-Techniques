
import torch
class Model(torch.nn.Module):
    def __init__(self, splitSize, dim=0):
        super().__init__()

    def forward(self, x1):
        splitted = torch.split(x1, splitSize) # split into several tensors along a given dimension using `torch.split`
        concatenated  = torch.cat([splitted[i] for i in range(len(splitSize))], dim=0) # concatenate the split tensors along the same dimension using `torch.cat`
        return concatenated

model = Model(2,1)
input_tensor = torch.randn((64, 3 ,35,89))

print(model(input_tensor).size())
