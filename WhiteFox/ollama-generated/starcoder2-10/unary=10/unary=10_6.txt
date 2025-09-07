
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(128, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 3
        v2 = F.relu6(v1).clamp_min(0).clamp_max(6)/ 6
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 4) # Assuming that the input tensor has a shape of (5, 4) for this example
__output__  = m(x1)

