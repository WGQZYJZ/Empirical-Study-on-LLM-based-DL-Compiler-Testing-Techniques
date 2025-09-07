
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x, other):
        v1 = torch.sigmoid(self.linear(x))
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()

