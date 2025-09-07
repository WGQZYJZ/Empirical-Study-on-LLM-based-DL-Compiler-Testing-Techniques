
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1  = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = mm1(x1)
        return t7


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 32)
