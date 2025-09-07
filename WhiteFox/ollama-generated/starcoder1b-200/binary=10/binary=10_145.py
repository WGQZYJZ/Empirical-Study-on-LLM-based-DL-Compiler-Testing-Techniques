
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 3)
 
    def forward(self, x):
        v = self.linear(x) + other
        return v


# Initializing the model
m = Model()

