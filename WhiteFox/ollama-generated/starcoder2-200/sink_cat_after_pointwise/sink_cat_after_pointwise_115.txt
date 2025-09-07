
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.relu(x1)
        return 64 * (v1.view(20, -1).max(dim=0)[0] + x1.norm() + v1.var())

# Initializing the model