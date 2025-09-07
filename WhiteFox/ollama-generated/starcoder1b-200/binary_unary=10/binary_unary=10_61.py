
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x):
        v1 = self.linear(x)
        return v1 + 1


# Initializing the model
m = Model()


