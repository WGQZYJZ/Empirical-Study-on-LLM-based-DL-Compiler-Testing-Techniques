
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + torch.randn_like(v1).cuda() # Generate random tensor for each iteration
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m  = Model().to('cuda')
 
# Inputs to the model
x1  = torch.randn(8, 3, 64, 64).to('cuda') # Generate random input tensor for each iteration
__output__  = m(x1)