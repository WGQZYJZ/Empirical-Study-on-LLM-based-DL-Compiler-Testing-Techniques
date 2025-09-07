
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        v1 = self.linear(x) + other
        return v1


# Initializing the model
m = Model()

