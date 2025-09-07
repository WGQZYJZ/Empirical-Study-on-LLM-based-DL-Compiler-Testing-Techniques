
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x):
        return self.linear(x) + 100

 # Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn(1, 32)
