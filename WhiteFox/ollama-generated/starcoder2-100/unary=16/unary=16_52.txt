
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc  = torch.nn.Linear(784,10)
 
    def forward(self, x):
        v2 = torch.nn.functional.relu(self.fc(x))
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x  = torch.randn(64,784)
