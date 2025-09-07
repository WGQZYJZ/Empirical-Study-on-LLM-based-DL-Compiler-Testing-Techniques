
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(64 * 64 * 3, 8)
 
    def forward(self, x1):
        v1 = self.lin(x1) # Apply a linear transformation to the input tensor
        v2 = torch.tanh(v1)# Apply tanh function on output of linear transformation
        return v2


# Initializing model