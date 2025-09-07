
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 10)
 
    def forward(self, x):
        v = x.view(-1, 28*28)
        v = self.linear(v)
        return torch.sigmoid(v)


# Initializing the model
m = Model()

