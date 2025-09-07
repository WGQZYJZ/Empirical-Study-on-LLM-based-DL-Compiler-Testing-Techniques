
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(50, 64)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x2):
        v7 = self.fc1(x2)
        v8 = self.relu(v7) 
        return v8

# Initializing the model
m = Model()

 # Inputs to the model 
x2  = torch.randn(50).view(1, -1)
__output__  = m(x2)
 
