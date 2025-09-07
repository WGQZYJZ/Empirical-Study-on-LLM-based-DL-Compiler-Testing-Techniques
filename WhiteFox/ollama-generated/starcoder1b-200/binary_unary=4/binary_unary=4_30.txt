
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)
 
    def forward(self, x1):
        return self.linear(x1) + 5


# Initializing the model
m = Model()
other = torch.randn(10)
