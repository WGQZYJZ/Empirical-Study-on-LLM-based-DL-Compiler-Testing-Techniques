
class Model(torch.nn.Module):
    def __init__(self, dim1, dim2, dim3):
        super().__init__()
        self.linear = torch.nn.Linear(dim1, dim2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 0.5
        return v2


# Initializing the model
m = Model(3, 4, 6)

# Inputs to the model
input_tensor = torch.randn(1, 3, 32, 32)
other = 1
