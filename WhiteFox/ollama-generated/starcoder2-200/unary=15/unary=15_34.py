
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1  = conv(x)
        v2 = relu(v1)
 
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
input_tensor=torch.randn(3, 5, 4096, 872)

m(input_tensor)

