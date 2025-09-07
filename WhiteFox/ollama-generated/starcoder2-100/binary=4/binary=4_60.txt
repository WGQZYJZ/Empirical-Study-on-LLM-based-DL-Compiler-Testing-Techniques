
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 256)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v1


m  = Model()
 
 # Inputs to the model
 x1 = torch.randn(32, 100)
 