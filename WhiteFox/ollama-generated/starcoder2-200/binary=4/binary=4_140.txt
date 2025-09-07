

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1) # Applying linear transformation to the input tensor
        v2  = v1 + other_tensor # Adding another tensor 
        return v2

# Initializing the model
m = Model()
other_tensor = torch.randn(v1.size()) # Other tensor with the same size as v1

