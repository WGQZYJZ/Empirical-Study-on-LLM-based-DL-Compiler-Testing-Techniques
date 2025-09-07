
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 32)
 
    def forward(self, x):
        v = self.linear(x)
        return sigmoid(v)


# Initializing the model
m = Model()


