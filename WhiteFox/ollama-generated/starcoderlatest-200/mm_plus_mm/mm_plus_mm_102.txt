
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Linear(3, 5)
        self.layer2 = torch.nn.Linear(64*32, 1024)
 
    def forward(self, x1, x2):
        v1 = self.layer1(x1)
        v2 = torch.mm(v1.view(-1, 64, 32), self.layer2.weight) + \
             self.layer2.bias
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8*32)
