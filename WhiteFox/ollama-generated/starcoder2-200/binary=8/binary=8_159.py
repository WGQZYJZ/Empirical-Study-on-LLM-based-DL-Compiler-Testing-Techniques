
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        
        # Use the "other" keyword argument in addition operator to add a constant 50 to the output of the convolution
        v2 = v1 + kwargs['other'] 
        return v2

# Initializing the model with constant 50 as the keyword argument for the addition operation
m = Model(other=torch.tensor([[[[50]]]]))

 # Inputs to the model
 x1  = torch.randn(1, 3, 64, 64)
 
 # Obtaining output of the model with keyword argument
 