
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(64, 320) # The dimension of x1 should be equal to [batch size] * [number of elements per input].
