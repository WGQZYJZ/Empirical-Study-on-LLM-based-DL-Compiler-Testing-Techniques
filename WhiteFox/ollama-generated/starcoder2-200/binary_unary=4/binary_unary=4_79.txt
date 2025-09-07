
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0  = self.linear(x1)
        v1  = v0 + other 
        v2  = torch.relu(v1)


# Initializing the model
m = Model()

other  = torch.randn(3)
__output__  = m(x1, other=other)

