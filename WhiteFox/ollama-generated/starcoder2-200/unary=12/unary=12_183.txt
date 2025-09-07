
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v0 = torch.ones_like(x1)
        v1 = conv(v0) 
        v2 = sigmoid(v1)
        v3 = v1 * v2
        return v3

# Initializing the model 
m  = Model()

 # Inputs to the model 
 x1  = torch.randn(1,3,64,64)
 __output__  = m(x1) 

 