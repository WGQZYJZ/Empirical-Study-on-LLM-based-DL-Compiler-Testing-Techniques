
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1

 # Initializing the model
m  = Model()

 # Input to the model 
 x2 = torch.randn(3072)
 
 # Inputs to the model
 x1 = torch.randn(8, 96, 57, 49)
 
