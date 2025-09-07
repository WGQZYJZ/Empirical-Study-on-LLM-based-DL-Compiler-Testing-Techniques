
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0 = [4] # Scalar
        v1 = self.conv(x1) 
        v2 = v1 - other  # Subtract a tensor or scalar "other" from the output of the convolution.
        v3 = torch.relu(v2 + v0[0])
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
other = torch.zeros_like(v2) # The model requires this tensor as an input (The name and type of "other" are irrelevant). This value is not important because it will be replaced with another value during the evaluation.
