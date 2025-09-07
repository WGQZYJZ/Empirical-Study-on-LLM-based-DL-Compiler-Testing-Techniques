
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       v1 = torch.nn.functional.linear(x1) # Apply linear transformation to the input tensor.
       v2  = v1.permute(0, 3, 1, 2).sum(-3) 
       return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(5, 3, 4, 6) # The shape of the input tensor is different from that of the previous one. 
__output__  = m(x1)
