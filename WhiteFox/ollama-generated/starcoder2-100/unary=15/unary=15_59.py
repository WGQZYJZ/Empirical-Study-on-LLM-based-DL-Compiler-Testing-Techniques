
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1): 
        v1  = self.conv(x1) 
        v2 = nn.functional.relu(v1)
        return v2

# Initializing the model
m  = Model() 

# Inputs to the model 
x1 = torch.randn(1,3,64,64) # Generate a random input tensor of shape [batch size x channel x height x width]
__output__= m(x1)

