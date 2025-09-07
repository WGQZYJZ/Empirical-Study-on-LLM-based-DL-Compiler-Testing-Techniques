
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 7, padding=0)
 
    def forward(self, x):
        v1  = self.conv1(x)
        v2  = v1 + torch.rand_like(v1)
        v3  = F.relu(v2) # The ReLU activation function is removed in this example
        return v3


# Initializing the model
m  = Model()

# Input to the model
x  = torch.randn(8, 3, 64, 64)
__output__  = m(x)

