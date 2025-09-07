
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.Conv1d(3, 8, 1)
        self.fc   = torch.nn.Linear(3, 10)
 
    def forward(self, x1):
        v1 = self.conv1d(x1)
        v2 = torch.matmul(v1, self.fc.weight)
        return v2


# Initializing the model
m = Model()
__input__ = torch.randn(3, 8, 50)
x1 = m(__input__)


