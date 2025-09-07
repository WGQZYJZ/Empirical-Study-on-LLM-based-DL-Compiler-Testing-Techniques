
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(40, 8)
 
    def forward(self, x1, x2):
        y1 = self.fc(x1)
        y2 = self.fc(x2)
        return torch.cat([y1, y2], dim=1)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(300, 40)
x2  = torch.randn(200, 8)
