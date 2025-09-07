
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input_tensor  = torch.randn(320,) # Input tensor has shape (320,) or (64, 5) in this example
other  = torch.randn(10,) # Other input tensor has shape (10,)
__output__  = m(input_tensor, other=other)

