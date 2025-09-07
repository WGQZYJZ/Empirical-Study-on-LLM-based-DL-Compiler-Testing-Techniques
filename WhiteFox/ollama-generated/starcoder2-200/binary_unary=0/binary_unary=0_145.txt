
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2   = v1 + other 
        v3   = torch.relu(v2)
        return v3

# Initializing the model
m  = Model()
other  = torch.randn(4096, requires_grad=True).detach() # Creating a new randomly generated tensor for "other"
 
# Inputs to the model (with other)
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1, other)

