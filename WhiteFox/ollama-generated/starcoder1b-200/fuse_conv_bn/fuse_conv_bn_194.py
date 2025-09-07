
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(...)  # ...can be a convolution or activation function

    def forward(self, x1):
        return self.linear(x1)  # ...


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(...)
