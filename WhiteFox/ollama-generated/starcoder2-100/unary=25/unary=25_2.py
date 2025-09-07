
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32 * 32, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        negative_slope  = 1e-5
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
 
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(64, 32*32)

 # The following line is an assertion statement that will raise an exception if 
# the output of the model does not match the expected result in this particular example.
