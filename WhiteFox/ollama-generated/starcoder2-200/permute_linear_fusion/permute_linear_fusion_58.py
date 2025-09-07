
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1[:, :, None]  # Make the third dimension as size 1 (which will be used to store the output).
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(30, 40, 50) # Input tensor, size [N, 50, 40] where N= 30, 40 and 50 are some fixed numbers
__output__  = m(x1)
