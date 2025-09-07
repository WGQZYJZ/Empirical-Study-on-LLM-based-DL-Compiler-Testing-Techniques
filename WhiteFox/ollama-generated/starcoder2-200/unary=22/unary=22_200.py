
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Add a new forward method to the model class
        return torch.tanh(x) + 5

