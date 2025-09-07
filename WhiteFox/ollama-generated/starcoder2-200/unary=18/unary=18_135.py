
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2 = torch.sigmoid(v1) 
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

 # Validating the model output with reference
ref_output = torch.sigmoid(m(x1))
__output__  = m(x1)
assert torch.allclose(__output__, ref_output), "Model output doesn't match."
