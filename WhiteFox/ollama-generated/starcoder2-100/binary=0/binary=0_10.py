
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, other=None): # Adding "other" as a keyword argument here allows us to add any constant tensor we like
        v1  = self.conv(x1)
        if other is not None:
            v4 = torch.add(v1, other)
        else:
            v4 = v1 + other
        return v4


# Initializing the model with a keyword argument
m = Model()
 
# Inputs to the model with 2 keyword arguments 
x1 = torch.randn(1, 3, 64, 64) # First argument is the input tensor. 
                              # For "other", we'll pass torch.tensor([0], requires_grad=True), which is a constant tensor that will be optimized in the search process.
other = torch.tensor([0], requires_grad=True)
 
