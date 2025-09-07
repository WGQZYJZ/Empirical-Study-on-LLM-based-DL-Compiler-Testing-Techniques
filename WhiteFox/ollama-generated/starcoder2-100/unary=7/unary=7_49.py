
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(784, 200)
        self.linear2 = torch.nn.Linear(200, 100)
 
    def forward(self, x1):
        v1 = self.linear1(x1) # Linear transformation applied to the input tensor
        v2 = v1 * clamp(min=0, max=6, v1 + 3) # Multiplying the output of the linear transformation by the clamped output (clamped between 0 and 6) of the linear transformation added with `3`
        v3 = v2 / 6 # Divide the output of the multiplication by 6
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 784)
