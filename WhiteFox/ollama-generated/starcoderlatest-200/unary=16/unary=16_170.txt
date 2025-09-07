
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(32*32*3, 16)
 
    def forward(self, x1):
        v1 = self.fc(x1.view(x1.size()[0], -1))
        v2 = F.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
