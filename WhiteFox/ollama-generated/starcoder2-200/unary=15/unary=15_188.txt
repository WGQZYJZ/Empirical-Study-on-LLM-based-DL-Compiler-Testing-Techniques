
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = conv(x1)
        v4  = relu(v1) 
        return v6


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(250, 3, 780, 900))
 
 # Evaluating the model
__output__  = m(x1)