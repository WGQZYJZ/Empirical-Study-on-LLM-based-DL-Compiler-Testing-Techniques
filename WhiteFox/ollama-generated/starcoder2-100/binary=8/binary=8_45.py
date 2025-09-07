
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.other = other
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 + self.other

# Initializing the model
m_other = torch.ones([5], requires_grad=True)
m  = Model(m_other)

 # Inputs to the model
 x = torch.randn(3, 3, 64, 64)
 
 # Calculating the output of our model
 