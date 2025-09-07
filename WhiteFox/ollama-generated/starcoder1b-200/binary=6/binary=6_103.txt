
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 0.5
        return v1


# Initializing the model
m = Model()

# Inputs to the model
input_tensor  = torch.randn(1, 32) # 'input' tensor for the linear transformation
__output__   = m(input_tensor) # Output of the linear transformation

