
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.relu(torch.cat([x1, x2], dim=0).view(-1))

