
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(4, 16)
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2, 0.1)
        v2 = self.fc(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 4, 512)
x2 = torch.randn(2, 16, 32)
