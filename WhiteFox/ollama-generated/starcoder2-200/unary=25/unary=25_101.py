

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 25)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v3 = -2 + (v1 * (-2)) + ((~v1) * (~(-2)))
        return v3

# Initializing the model
m = Model()

