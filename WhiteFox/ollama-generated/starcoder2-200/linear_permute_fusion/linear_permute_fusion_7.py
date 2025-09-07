

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, 10, bias=False) # The size of the bias is 2 but the bias=false makes it a 1d tensor.
        v3  = v1.permute([1])
        return v3


# Initializing the model
m  = Model()

# Inputs to the model.
x1 = torch.randn(1, 5) # The size of this input is 2 but the permute method requires that the size be one. 
x2 = m(x1)

