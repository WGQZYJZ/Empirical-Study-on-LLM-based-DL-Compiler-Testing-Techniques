
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, -1 * v1 * 0.001) # Implement LeakyReLU in PyTorch (LeakyReLUs may require different parameters for different input sizes; please refer to the official documentation: https://pytorch.org/docs/stable/nn.html#leakyrelu)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
