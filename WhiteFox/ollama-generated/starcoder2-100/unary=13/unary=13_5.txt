

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320*8, 1)
 
    def forward(self, x): 
        v1 = self.linear(x).view(-1, 4, 5) # Apply the linear transformation to the input tensor and reshape it.
        v2 = F.sigmoid(v1)                   # Pass the output of the linear transformation through a sigmoid function.
        return torch.sum(v2 * v1)             # Multiply the output of the linear transformation by the output of the sigmoid function, then take the sum across the resulting tensor.

# Initializing the model 
m = Model()


# Inputs to the model
x  = torch.randn(640*8)
