
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1, y1):
        v1  = x1.permute(dim, -1, 0) # Permute the input tensor
        v2  = torch.cat([v1, y1], dim=0)
        v3  = self.linear(v2)
        return torch.nn.functional.relu(v3)


# Initializing the model