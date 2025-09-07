
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
        self._other_tensor = torch.randn(4, 32, 56, 108)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self._other_tensor # Add another tensor to the output of the linear transformation
        return v2


# Initializing the model
m = Model()
# other=None means no argument is specified for "other". 

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
