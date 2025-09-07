
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Inputs to the model should be different from each other.
        return torch.randn(1024) + 6

