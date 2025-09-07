
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.randn(3) # Input tensor B. This value is not related to previous inputs or intermediate values
        v4  = torch.bmm(x1, v2)
        return v4


# Initializing the model