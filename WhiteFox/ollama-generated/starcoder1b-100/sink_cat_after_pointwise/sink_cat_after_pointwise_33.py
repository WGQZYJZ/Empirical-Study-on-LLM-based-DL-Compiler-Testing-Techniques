
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        # Concatenate tensors along a dimension
        v1 = torch.cat([x1, x2], dim=0)

        # Reshape the concatenated tensor
        v2 = v1.view(-1, 4)
        v3 = torch.relu(v2)

        return v3


# Initializing the model
m = Model()
x1 = torch.randn(2, 2, 4)
