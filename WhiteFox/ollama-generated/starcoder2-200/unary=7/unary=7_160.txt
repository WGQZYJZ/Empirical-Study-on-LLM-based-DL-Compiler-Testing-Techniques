
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4,16)
    
    def forward(self, x1):
        v0  = self.linear(x1) # Apply linear transformation to the input tensor.
        v2  = clamp(min=0, max=7, value=v0 + 3) # Clamp the linear transformation of the input tensor added with `3`.
        v4  = v2 / 6 # Divide the linear transformation by 6.
        return v4


# Initializing the model
m  = Model()
# Inputs to the model: A dummy data
input_tensor = torch.randn(1,4)
__output__  = m(input_tensor)