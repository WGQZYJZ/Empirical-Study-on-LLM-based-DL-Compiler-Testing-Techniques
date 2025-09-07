
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1):
        v2  = self.linear(x1).permute(0, 2, 1) # Swapped dimensions of the output tensor from permute operation
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3, 4, 6)  # The input tensor has a shape of (3, 4, 6).
__output__  = m(x1)

