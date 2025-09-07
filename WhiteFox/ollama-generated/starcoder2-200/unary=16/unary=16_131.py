
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v1  = self.fc(x1) 
        v2  = torch.nn.functional.relu(v1)
        return v2


# Initializing the model
m = Model()
__output__  = m(torch.randn(64, 784))
