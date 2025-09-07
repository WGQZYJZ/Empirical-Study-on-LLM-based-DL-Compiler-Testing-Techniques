
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v1

 # Initializing the model
m = Model()
 
 # Inputs to the model
x1 = torch.randn(2048*256//32*256//32*2, 3)
