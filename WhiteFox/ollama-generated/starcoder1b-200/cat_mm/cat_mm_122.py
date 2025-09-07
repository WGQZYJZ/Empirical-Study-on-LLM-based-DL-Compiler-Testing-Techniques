
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1, ..., v1], 1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
inputs = torch.randn(4, 64, 64, requires_grad=True)
outputs = m(inputs[0], inputs[1])


