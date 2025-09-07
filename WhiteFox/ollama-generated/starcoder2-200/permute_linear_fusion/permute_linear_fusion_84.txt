
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.empty([2, 3], requires_grad=True) # Create a temporary tensor.
        v4 = x1.permute(0, 2, 1)
        return (v3 @ v4).sum()


# Initializing the model