
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.cat([x1, x2], dim=0)
        v2  = v1.view(-1, 4, 5)
        v3  = torch.nn.functional.relu(v2[:, 1:])
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(20, 2).permute(0, 1).contiguous().view(-1, 4)
x2 = torch.zeros(18, 5)
__output__  = m(x1, x2)