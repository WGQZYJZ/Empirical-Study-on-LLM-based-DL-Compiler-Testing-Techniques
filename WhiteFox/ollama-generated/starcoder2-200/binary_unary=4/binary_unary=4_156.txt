
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 3)
 
    def forward(self, x1):
        v0 = torch.nn.functional.relu(x1 + 64*7)
        return self.linear(v0)

m  = Model()

 # Inputs to the model