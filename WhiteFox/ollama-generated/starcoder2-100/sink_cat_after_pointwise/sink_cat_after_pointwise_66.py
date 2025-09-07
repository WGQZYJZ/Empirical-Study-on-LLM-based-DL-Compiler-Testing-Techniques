
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()

    def forward(self, x1):
        v2  = torch.cat([x1, x1], axis=0)
        v3  = v2.view(-1)
        return torch.relu(v3)


# Initializing the model
m  = Model()
__output__  = m(torch.randn(5, 1))