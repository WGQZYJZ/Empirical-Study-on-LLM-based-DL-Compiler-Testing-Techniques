
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 48)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is not None:
            v2 = v1 + other
        return v2


# Initializing the model
m = Model()
other = torch.randn(48) # Initialize another tensor to be added to the output of the linear transformation

# Inputs to the model
x1 = torch.randn(1, 16, 3, 32, 32)
