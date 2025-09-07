
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
 
    def forward(self, x):
        v  = self.linear(x) + 3
        return v


# Initializing the model
m = Model()


