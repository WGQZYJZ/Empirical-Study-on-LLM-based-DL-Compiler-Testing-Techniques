
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(7, 2)
 
    def forward(self, x):
        v  = self.linear(x) * torch.randn_like(v).exp_()
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
