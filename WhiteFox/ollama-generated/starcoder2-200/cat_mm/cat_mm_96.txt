
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
        self.mm = torch.nn.Linear(input1 * input2, 3)
 
    def forward(self, x1):
        v1 = self.mm(x1)
        return torch.cat([v1, v1])


# Initializing the model
m = Model(8, 64)


# Inputs to the model
x1 = torch.randn(257, 32 * 64)


__output__  = m(x1)

