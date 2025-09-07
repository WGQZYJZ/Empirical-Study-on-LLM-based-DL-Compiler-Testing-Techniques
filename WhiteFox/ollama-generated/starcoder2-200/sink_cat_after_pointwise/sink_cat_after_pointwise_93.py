
class Model(torch.nn.Module):
    def __init__(self, linear):
        super().__init__()
        self.linear = linear

    def forward(self, x1):
        v1  = torch.cat([x1, ...], dim=...)
        v2  = v1.view(-1)
        v3  = torch.relu(v2)
        return v3


# Initializing the model