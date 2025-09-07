
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(28 * 28, 50)
        self.linear2 = torch.nn.Linear(50, 30)
 
    def forward(self, x):
        v1 = self.linear1(x.view(-1, 28 * 28))
        v2 = self.linear2(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(32, 1, 28, 28)
