
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 5)
 
    def forward(self, x1, other=None):
        return self.linear(x1), other + 4


# Initializing the model
m = Model()

