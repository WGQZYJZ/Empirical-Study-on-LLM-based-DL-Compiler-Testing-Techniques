
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
 
    def forward(self, x):
        return self.linear(x) - 5
 
 # Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(3, 2)
