
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 64)
 
    def forward(self, x):
        v1 = self.linear(x)
        return v1 * torch.sigmoid(__output__)


# Initializing the model
m = Model()
__input__ = torch.randn(1, 3, 64, 64)
