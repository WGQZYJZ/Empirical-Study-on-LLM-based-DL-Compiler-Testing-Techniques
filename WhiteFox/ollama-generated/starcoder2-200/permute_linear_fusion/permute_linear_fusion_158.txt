
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1) # Permute the input tensor
        v3  = v1.permute(0, 2, 1) # Permute again to restore the shape back
        v4  = torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 5, 3)
