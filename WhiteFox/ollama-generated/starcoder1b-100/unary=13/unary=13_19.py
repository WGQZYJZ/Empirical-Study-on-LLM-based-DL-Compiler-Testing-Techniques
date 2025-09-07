
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 1)
 
    def forward(self, x):
        v  = self.linear(x)
        v  = sigmoid(v)
        return v


# Initializing the model
m = Model()
__input__ = torch.randn(1, 8)
