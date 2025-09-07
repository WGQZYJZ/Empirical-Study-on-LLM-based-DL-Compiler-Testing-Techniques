
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
    	return torch.split(x1, 50, dim=3)[4]

 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(28, 16, 1000)
 
