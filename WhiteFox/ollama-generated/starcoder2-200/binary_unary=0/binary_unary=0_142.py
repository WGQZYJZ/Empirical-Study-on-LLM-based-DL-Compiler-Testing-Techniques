
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other
        v3  = F.relu(v2)
        return v3


# Initializing the model
m  = Model()
 
 # Inputs to the model
other  = torch.randn(1, 8, 64, 64).to('cuda')
x1     = torch.randn(1, 3, 64, 64)
x2     = torch.randn(1, 3, 64, 64)
 
output1 = m(other) # A tensor that is not used for the forward pass of the model
output2 = m(x1).to('cuda') + output1.to('cuda')
 

