
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.cat([x1, x2], dim=3)
        v2  = v1.view(-1, 4*v1.shape[3])
        v3  = torch.relu(v2) # Unary operation
        return v3

# Initializing the model