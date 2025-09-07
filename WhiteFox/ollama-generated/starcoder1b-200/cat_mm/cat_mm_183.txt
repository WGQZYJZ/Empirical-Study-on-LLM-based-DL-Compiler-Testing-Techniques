
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m = torch.nn.Linear(3, 64)
 
    def forward(self, x1):
        v1 = self.m(x1)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 2, 3, 64, 64)
x2  = x1.view(-1, 3 * 64)
