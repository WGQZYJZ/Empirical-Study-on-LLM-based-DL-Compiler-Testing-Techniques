import torch 

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.dropout(x1)
        return v2
m  = Model()

x1 = torch.rand(3049, 857, 608)
