
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2, t3):
        v1 = torch.cat([t1, t2, t3], dim=0)
        v2 = v1.view(-1)
        return v2


# Initialization of the model
m = Model()

# Inputs to the model
t1 = torch.randn(10, 4)
t2 = torch.randn(5, 3, 4)
t3 = torch.randn(6, 7)
