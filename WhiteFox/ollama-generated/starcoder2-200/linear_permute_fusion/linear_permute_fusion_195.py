
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, 0)
        v4  = v3.permute(2, 1, 0) # Permute the 3rd and last dimensions of this tensor
        return v4

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(512, 8, 8)
__output__  = m(x1)
