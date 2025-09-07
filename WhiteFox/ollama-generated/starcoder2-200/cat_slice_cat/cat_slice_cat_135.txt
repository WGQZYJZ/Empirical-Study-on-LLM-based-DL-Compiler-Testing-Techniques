
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv(x[:, :9223372036854775807]) # Slice the input tensor along dimension 1 and concatenate the sliced tensor with its transpose along the same dimension
        v2 = torch.cat([v1, v1], dim=1) # Concatenate the concatenated tensor along dimension 1
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 950, 64)
__output__  = m(x)