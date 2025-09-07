
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 'other'  # 'other' is a string variable representing the scalar (int or float) that should be subtracted from the output of the linear transformation.
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 8)
__output__  = m(x1)