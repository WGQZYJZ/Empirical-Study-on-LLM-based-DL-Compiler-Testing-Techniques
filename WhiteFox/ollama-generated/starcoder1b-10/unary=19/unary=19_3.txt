
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 2)
 
    def forward(self, x1):
        v1 = x1.view(-1, 784)
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model()

