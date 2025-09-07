
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.add(x1[0], x1[1])  # Add two tensors together.
        return v1


# Initializing the model