
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 49 * 30 + 387, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply the linear transformation to the input tensor
        
        v2  = v1 + other # Add another tensor to the output of the linear transformation
        
        return v2


# Initializing the model
m = Model()
other = torch.rand(v1.shape[0], requires_grad=True)

# Inputs to the model
x1  = torch.randn(7, 518493 + 387) 
