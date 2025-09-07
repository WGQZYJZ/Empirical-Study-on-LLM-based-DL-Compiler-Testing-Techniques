

class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v4  = clamp(min=0, max=6, input)
        v5  = torch.erf(v2  + 3) # Apply the error function to the output of the linear transformation added with `3`
        return v5


# Initializing the model
m1  = Model()

