
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 1)
 
    def forward(self, x):
        y = self.linear(x)
        return torch.sigmoid(y)


# Initializing the model
m = Model()

