
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).type_as(v1)
        v3  = v1 * negative_slope 
        v4  = torch.where(v2, v1, v3)

        return v4

# Initializing the model with a given value for the negative slope argument.
negative_slope  =  0.5
 
m = Model(negative_slope)

 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 
 __output__  = m(x1)
 
 # Sample input tensor to avoid error.
 input = [0.,  0., -7.]
 
# Input tensor for testing.
input_tensor = torch.tensor([[input]])

print(input_tensor)<jupyter_output><empty_output>