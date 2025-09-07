
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 32 * 32 + 64 * 32, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Applies a linear transformation to an input tensor
        return v1

# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(32*8 + 64 * 32, requires_grad=True)
__output__  = m(input_tensor)

