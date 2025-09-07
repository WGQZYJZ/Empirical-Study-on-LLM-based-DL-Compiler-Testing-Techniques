
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.randn([3]) # Add another tensor as a keyword argument to the addition operation
        v1  = self.conv(x1)
        return v1 + v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

