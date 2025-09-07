
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1  = torch.mm(x1, x2)
        return torch.cat([t1, t1, ..., t1])


# Initializing the model
m  = Model()


# Inputs to the model
inputs  = [torch.randn(10, 3, 64, 64), torch.randn(10, 5)]
