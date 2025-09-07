
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        return self.linear(x1) + 0.1 * self.linear(x1).pow(2)


# Initializing the model
m = Model()

