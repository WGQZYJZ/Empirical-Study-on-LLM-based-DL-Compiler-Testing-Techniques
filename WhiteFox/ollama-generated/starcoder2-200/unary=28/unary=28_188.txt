
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2  = torch.clamp_min(v1, -0.5) # Clamp the output of the previous operation to a minimum value
        v3  = torch.clamp_max(v2,  4.5) # Clamp the output of the previous operation to a maximum value
        return v3


# Initializing the model and input tensor for the model.
m1 = Model()
x1  = torch.randn(8, 3)

__output_1__  = m1(x1)

