
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(256, 3)
 
    def forward(self, x1):
        v1  = self.lin(x1) 
        v2  = F.relu(v1) # Apply ReLU activation function to the output of the linear transformation.
        return v2


# Initializing the model
m = Model()
 
# Input tensors for the model
x1_input  = torch.randn(3, 50, 4, 8).float() 
x2_input  = torch.randn(7569) # A random tensor of shape (7569,) or (15, 7569).
 

