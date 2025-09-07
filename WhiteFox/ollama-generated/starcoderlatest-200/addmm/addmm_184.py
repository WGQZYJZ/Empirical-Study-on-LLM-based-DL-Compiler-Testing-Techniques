
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1, self.weight) + inp 
        return v2
        
m = Model() # Initialize the model
x  = torch.randn(10, 5, 3) # Inputs to the model (keyword argument is missing)
w  = torch.randn(784, 10) # Weights of the linear layer (keyword argument is missing) 

