
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(2048, 512)
        self.relu1 = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = self.relu1(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 512, 384, 256)
