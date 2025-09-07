
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)
 
    def forward(self, x1, other):
        return self.linear(x1 + other)


# Initializing the model
m = Model()

