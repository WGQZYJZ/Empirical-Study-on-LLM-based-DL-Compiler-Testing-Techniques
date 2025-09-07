
class Model(torch.nn.Module):
    def __init__(self, other=100):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x):
        return self.linear(x) + self.other
 
    @property
    def other(self):
        return 2


# Initializing the model
m = Model()


