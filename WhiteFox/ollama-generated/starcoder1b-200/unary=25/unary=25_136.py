
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1.0):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.linear(x1).abs()
        v2 = torch.where(v1 > 0.0, v1, self.negative_slope * v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 10, requires_grad=True)
x1.requires_grad_() # A PyTorch Variable that indicates that this tensor should be calculated and saved. Please use the .data property to obtain actual data from it after .backward() is invoked on it.
