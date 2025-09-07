
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 8)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        return v3 + other


# Initializing the model
m = Model()


