
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.convt(x1)  # pointwise transposed convolution of the input tensor
        v2 = torch.sigmoid(v1)
        return v2

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
