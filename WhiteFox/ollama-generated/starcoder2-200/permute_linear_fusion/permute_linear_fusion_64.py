
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # <-- This is where the new model should go!
        v1 = torch.permute(x1, (0, 2, 1))  # <--- Modifying the first model
        v2 = torch.nn.functional.linear(v1, 3)
	v3 = torch.nn.functional.linear(v2, 5)
        return v3


# Initializing a new model with two layers and inputs
m = Model()
m_x1  = torch.randn((2, 2, 2)) # <- You'll need 4 inputs here!
__output__  = m(m_x1)

# Input tensor
m0  = torch.randn(2, 3, 5, 7)