
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(25088, 43)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise linear transformation to the input tensor

        return v6

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 25088)
