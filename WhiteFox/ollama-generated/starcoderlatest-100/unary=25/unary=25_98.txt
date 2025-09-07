
class Model(torch.nn.Module):
    def __init__(self, num_layers=4):
        super().__init__()
        self.layer1 = torch.nn.Linear(32, 64)
        self.layer2 = torch.nn.Linear(64, 64)
        self.layer3 = torch.nn.Linear(64, 64)
 
    def forward(self, x):
        v1 = self.layer1(x)
        v2 = self.layer2(v1)
        v3 = self.layer3(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(4, 32, 64, 64)
