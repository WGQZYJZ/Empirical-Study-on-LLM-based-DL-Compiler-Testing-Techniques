
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split = torch.split([0, 1], [32])
        self.cat   = torch.cat(self.split)
 
    def forward(self, x1): 
        return x1 + self.cat
 
# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(64)
