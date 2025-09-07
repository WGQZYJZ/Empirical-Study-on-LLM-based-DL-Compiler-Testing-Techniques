
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8, bias=True)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * torch.clamp(v1 + 3, min=0, max=6)
        v3 = v2 / 6
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 3) # Input tensor of size (5, 3). Since there is no requirement for input shape other than (N, D), we use a dummy input with size (5, 3) here.
