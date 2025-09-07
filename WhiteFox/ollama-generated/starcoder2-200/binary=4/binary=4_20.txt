
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 257, 10)
 
    def forward(self, x1, other):
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor
        v2 = v1 + other # Add another tensor (specified by keyword argument "other") to the output of the linear transformation
        return v2


# Initializing and running model
m  = Model()
m(torch.randn(4,64*257), torch.zeros(4))

