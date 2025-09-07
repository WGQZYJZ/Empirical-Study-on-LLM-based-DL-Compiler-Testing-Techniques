

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, 200)
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(500)
