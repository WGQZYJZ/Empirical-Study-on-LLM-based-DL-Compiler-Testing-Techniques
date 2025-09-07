
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.tanh(x1)
        return v2
 
# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(10, 5, 34) # This is an input tensor that we want to test. The actual size of this tensor should be larger than the one defined above (for example, (68, 5, 34)).

__output__  = m(x1)

