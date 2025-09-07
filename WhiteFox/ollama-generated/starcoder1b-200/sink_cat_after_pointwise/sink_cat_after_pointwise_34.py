
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=1)  # Catenate two input tensors of shape (2, 2)
        return torch.relu(v1)


# Initializing the model
m = Model()

