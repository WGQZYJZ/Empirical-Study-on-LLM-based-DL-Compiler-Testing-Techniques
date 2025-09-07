
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.relu(x1) # Apply a ReLU to the input tensor
        v2  = self.conv(v1) 
        v3  = v2 + 3 
        v4  = torch.clamp(v3, min=0) 
        v5  = torch.clamp(v4, max=6) 
        v6  = v2 * v5  
        return v6 / 6


# Initializing the model
m  = Model()

 # Inputs to the model 
 x1  = torch.randn(1, 3, 97, 97).requires_grad_()
 

