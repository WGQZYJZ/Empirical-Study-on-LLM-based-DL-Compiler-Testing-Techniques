
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(-10, -2)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0 
        v3  = v1 * negative_slope  
        v4  = torch.where(v2, v1, v3)
        
        return v4


# Initializing the model and feeding it with an input tensor for example purposes:

m  = Model()
x1 = torch.randn(50)
