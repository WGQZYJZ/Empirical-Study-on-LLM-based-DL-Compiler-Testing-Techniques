
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 3)
 
    def forward(self, x):
        return self.linear(x).squeeze(-1)


# Initializing the model
m = Model()


# Inputs to the model
__input__ = torch.randn(1, 3, 64, 64)
