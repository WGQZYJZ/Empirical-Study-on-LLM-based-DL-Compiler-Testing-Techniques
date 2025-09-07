
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 5)
 
    def forward(self, x):
        v1 = self.linear(x)
        return v3 + v2


# Initializing the model
m = Model()


