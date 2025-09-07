
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1], dim=0)  # Concatenate tensors along a dimension (dimension 0 is the batch dimension).
        v2 = v1.view(-1, 3, 4)
        v3 = F.relu(v2 + self._param)
        return v3


# Initializing the model