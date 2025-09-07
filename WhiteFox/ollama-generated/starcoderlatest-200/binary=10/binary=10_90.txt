
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + x2 # Add another tensor to the output of the linear transformation
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.rand(1, 2, 64, 64) # An input tensor of size [1, 2, 64, 64]
