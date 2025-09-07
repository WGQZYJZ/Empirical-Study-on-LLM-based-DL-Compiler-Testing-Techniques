
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.convT(x1)
        v2 = self.relu(v1)
 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1,3,64,64)
 
# Executing the forward pass of the model (for a single batch/sample in our case)
__output__  = m(x1)

