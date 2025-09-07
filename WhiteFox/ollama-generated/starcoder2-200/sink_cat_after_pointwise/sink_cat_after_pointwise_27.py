
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0)
        v2 = v1.view(-1, 137504) # <- Change to a fixed size tensor
        v3 = F.relu(v2)
        return v3

# Initializing the model
m = Model()

