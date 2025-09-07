
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1e-6):
        super().__init__()
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = x1 * self.negative_slope  # Multiply the input tensor by the negative slope
        return torch.where(x1 > 0, x1, v1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
