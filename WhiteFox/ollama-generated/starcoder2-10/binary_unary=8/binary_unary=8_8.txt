
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) + torch.randn_like(v1).to('cuda')
        v4  = torch.relu(v3) # Apply the ReLU activation function to the result
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64).to('cuda')
__output__  = m(x1)

