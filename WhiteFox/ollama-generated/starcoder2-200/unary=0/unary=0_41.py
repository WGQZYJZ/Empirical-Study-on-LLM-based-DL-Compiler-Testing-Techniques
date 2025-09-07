
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 *  0.5 
        v3  = v1 * torch.pow(v1, 3.)
        v4  = v3 * -0.894427190999916
        v5  = v1 + v4  
        v6  = v5 *  1.9990893307783355 
        v7  = v2 * torch.tanh(v6)
        return v7

 # Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 42, 42)

 