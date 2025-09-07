
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32768 * 10 + 1536 + 4, 9)
 
    def forward(self, x1, other): # the argument 'other' is provided to the model for convenience
        v1 = self.lin(x1) + other
        return v1


# Initializing the model with input tensor of size `327680 * 10` and input tensor of size `(1536+4)` as an argument:
m = Model()
_ = m((torch.randn(32768*10), torch.randn(1536 + 4)))

