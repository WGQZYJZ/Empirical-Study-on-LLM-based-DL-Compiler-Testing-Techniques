
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 30)
 
    def forward(self, x1):
        v1 = torch.reshape(x1, (1, -1))
        v2 = self.linear(v1)
        return v2 + other


# Initializing the model
m = Model()


