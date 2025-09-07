
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.relu(torch.cat([x3, x4], dim=0).view(-1, 5))
        return v2

# Initializing the model