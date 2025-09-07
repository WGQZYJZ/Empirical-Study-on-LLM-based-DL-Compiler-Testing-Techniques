
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(128, 64)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min=-500)
        v3 = torch.clamp_max(v2, max=700)

# Initializing the model 
m = Model()

# Inputs to the model
x1 = torch.randn(128, requires_grad=True) # The input tensor is of shape (batch size, channels), and it will have a gradient w.r.t. its elements 

# Running the model on the inputs and taking the loss with respect to the model parameters 
__output__,  __loss__ = m(x1), -torch.sum(m.parameters())

# Taking the backward pass
__loss__.backward()

