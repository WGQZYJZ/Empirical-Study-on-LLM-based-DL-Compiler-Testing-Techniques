
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(28*28, 10)
 
    def forward(self, x1):
        v1 = self.fc(x1.view(-1, 28*28))
        v2 = torch.relu(v1)
        return v2


# Inputs to the model
x1 = torch.randn(4, 1, 28, 28)
