
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2a = (v1 >  0).float() # True is for elements in v1 greater than 0 and False otherwise. This mask is used to exclude the negative slope from multiplication with negative_slope.
        v3 = negative_slope * torch.where(v2a, v1, -negative_slope)
        return v3

# Initializing the model<|end_of_model|>
m  = Model()
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

