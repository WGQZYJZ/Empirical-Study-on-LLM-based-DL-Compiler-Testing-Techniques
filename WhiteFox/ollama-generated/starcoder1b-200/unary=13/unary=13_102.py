
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 2)
 
    def forward(self, x):
        v1 = self.linear(x)
        return sigmoid(v1)


# Initializing the model
m = Model()


