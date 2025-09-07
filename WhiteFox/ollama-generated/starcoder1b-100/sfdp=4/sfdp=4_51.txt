
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(768, 128)
        self.fc2 = torch.nn.Linear(128, 1000)
 
    def forward(self, x1):
        v = self.fc1(x1)
        v = self.fc2(v)
        return v

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 768)
y1 = m(x1)

 