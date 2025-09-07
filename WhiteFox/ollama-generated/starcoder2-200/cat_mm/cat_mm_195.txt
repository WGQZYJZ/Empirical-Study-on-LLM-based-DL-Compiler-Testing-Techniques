

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        v1 = torch.mm(input1, input2)
        return torch.cat([v1, v1])


# Initializing the model
m  = Model()

# Inputs to the model
i1  = torch.randn(50, 43, 98, 76)
i2  = torch.randn(50, 43, 98, 76)
__output__  = m(i1, i2)

