
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16)
 
    def forward(self, x):
        v = self.linear(x)
        return negative_slope * v


# Initializing the model
m = Model()


