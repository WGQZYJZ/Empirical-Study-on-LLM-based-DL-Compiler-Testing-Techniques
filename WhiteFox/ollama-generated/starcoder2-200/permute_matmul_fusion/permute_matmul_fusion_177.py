
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1  = x1.permute(0, 2, 1)
        t3  = torch.bmm(t1, x2) 
        return t3


# Initializing the model
m  = Model()


# Inputs to the model (Note that we have two input tensors here.)
x1 = torch.randn(100, 54987, 6)
x2 = torch.randn(100, 6, 3)
