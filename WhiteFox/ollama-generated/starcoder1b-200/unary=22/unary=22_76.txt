
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 192, 5)
 
    def forward(self, x):
        v  = x @ torch.randn(5) + 0.5
        return v


# Initializing the model
m = Model()

