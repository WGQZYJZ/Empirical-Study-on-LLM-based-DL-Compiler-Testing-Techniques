

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1) + 3

        v2 = torch.clamp(v1, min=0.) # clamp_min
        v3 = torch.clamp(v2, max=6.) # clamp_max
        return v3 / 6.


# Initializing the model
m = Model()
x1 = torch.randn(5) # Shape: [B]
x2 = torch.empty((3,), dtype=torch.int8).random_(0, 197) # Shape: [B]

# Inputs to the model
__output_1__, __output_2__  = m(x1), m(x2)

