
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
        v1 = torch.cat([t1, t2], dim=0)
        v2 = v1.view((v1.shape[0]*v1.shape[1]))
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 3, 2)
