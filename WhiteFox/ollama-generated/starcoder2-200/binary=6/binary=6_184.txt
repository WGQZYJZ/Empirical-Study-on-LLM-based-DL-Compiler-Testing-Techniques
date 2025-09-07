
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


# Initializing the model
m  = Model()
# Inputs to the model
x1  = torch.randn(3, 256)
__output__  = m(x1) # We expect this line to fail

__output__  = m(0.8 * x1) # The model is not broken; The input tensor is a constant 0.8 times larger than the input above