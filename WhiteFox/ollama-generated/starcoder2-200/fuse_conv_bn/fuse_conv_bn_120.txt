
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        return torch.nn.functional.conv2d(x1, 
                                          weight = torch.randn((3, 5)),  # Shape: [M, N]
                                          bias   = None)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.rand(size=(1,28,28))

# Executing the model with `torch.enable_grad` 
with torch.no_grad():
    __output__  = m(x1)

