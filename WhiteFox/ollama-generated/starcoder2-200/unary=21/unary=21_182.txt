
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
         v1 = self.conv(x1)
         v2 = torch.tanh(v1) # tanh(v1)
         return v2
# Initializing the model
m  = Model()
__output__  = m(x1)

# Inputs to the model: 1.5 times 0.3141592653589793
x1 = torch.tensor([[1., -1.,  1., .3, -.7], 
                   [ 1., -1.,  1., .3, -.7]])

# Initializing the model: 
m(x1)

-0.6428956365585327
