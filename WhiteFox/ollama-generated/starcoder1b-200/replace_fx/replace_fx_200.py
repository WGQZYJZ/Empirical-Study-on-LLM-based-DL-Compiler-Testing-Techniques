
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @replace_fx  # Replace this with a corresponding replacement function
    def forward(self, x1, t2=0.5):
        return torch.sigmoid(x1) * t2


# Inputs to the model
x1 = torch.randn(1, 3, 4)
