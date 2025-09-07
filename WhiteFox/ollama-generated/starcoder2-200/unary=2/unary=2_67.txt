
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.convT(x1)
        v2  = v1 * 0.5
        v3  = v2 * v2  # <== this is where the multiplication is used in this pattern (multiply the output of transposed convolution by another constant 0.7978845608028654)
        v4  = torch.tanh(v1 + v3 * 0.044715) 
        v5  = v2 + v4
        return v5


# Initializing the model with a given seed (for example, 1)
m  = Model()
m = torch.manual_seed(1)

