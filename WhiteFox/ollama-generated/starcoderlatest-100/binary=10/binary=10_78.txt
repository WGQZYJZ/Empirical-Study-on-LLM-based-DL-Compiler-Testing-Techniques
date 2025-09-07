
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*128, 50)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1.view(-1))
        if other is not None:
            v2 = v1 + other
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 64*128)
other = torch.randn(2, 50)
