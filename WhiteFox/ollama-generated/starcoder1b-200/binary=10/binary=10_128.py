
class Model(torch.nn.Module):
    def __init__(self, other=0):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other
        return v1


# Inputs to the model
input_tensor = torch.randn(2, 4, 64, 64)
other        = torch.randn(3, 8)
__output__   = Model(other=other)(input_tensor)


