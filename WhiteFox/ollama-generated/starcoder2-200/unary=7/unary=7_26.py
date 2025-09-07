
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.nn.functional.linear(x1)
        v2  = clamp(min=0, max=6, l1 + 3) 
        v3 = v0 * v2 # Multiplied output of the linear transformation by clamped output of the linear transformation added with `3`
        v4  = torch.nn.functional.relu(v3)
        v5 = v4 / 6
        return v5


# Initializing the model
m1, m2 = Model(), Model()

# Inputs to the model
x1 = torch.randn(1, 98776) 

__output_m1__, __output_m2__ = m1(x1), m2(x1)

