
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v0 = self.linear(x1) + v5 # where v5 is the tensor mentioned in the previous requirement
        return v0


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(32)


__output__  = m(x1)
