
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 1)
 
    def forward(self, x):
        v  = self.linear(x)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(3, 8, requires_grad=True)
x.requires_grad_()
