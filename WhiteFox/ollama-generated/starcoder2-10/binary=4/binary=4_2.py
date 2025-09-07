
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 * 10, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply linear transformation to input tensor
        v2  = v1 + torch.randn_like(v1)  # Add another tensor to the output of the linear transformation
        return v2

# Initializing the model
m  = Model()
 
# Inputs to the model (of the form [x1]) 
x1 = torch.randn(3, 64 * 320)

