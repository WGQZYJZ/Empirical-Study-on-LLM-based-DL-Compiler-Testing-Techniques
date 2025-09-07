
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1)) # Apply a linear transformation to the view of the input tensor with shape (n, c*h*w). In this case, h and w are both set to 1.
        v2 = v1 - 1 # Subtract 1 from the output of the linear transformation
        return v2


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(4, 3 * 64 * 64)
