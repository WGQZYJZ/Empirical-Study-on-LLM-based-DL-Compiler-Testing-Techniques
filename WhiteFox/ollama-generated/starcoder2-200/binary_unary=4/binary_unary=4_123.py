
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=0.5):  # This model also requires to pass an additional parameter
        v1 = self.linear(x1) + other   # The second output
        return torch.relu(v1)


m = Model()
__output__  = m(torch.randn(24), other=0.) # Passing an additional parameter to the model
