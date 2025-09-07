
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(768, 3)
 
    def forward(self, x1):
        x2 = F.relu(self.fc(x1))
        return x2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 768)
