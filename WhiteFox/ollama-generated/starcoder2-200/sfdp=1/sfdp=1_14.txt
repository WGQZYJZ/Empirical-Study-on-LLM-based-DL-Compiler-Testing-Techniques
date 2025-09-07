
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(16, 32)
        self.tanh    = torch.nn.Tanh()
 
    def forward(self, x):
        v1  = self.linear(x) # Apply a linear transformation to the input tensor
        v2  = self.tanh(v1)   # Apply the tanh function to the output of the linear transformation
        return v2
 
 # Initializing the model
m  = Model()

 # Inputs to the model 
 x1, x2, x3= torch.randn(64), torch.randn(8, 32), torch.zeros((50)) 
 
 
 
