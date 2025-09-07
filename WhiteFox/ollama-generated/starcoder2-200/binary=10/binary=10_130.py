
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.__output__
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(8096, 32)
__output__  = torch.randn(8096, 64)
__output__  # 0.5

# Generate the input tensor of the model m