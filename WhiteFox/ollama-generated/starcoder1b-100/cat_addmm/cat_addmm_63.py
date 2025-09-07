
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(4, 3)
 
    def forward(self, x1, x2):
        return self.fc(x1) + self.fc(x2)


# Inputs to the model
x1 = torch.randn(3, 4)
x2 = torch.randn(3, 3)
