
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = self.linear(x1)
        return self.linear(v1)


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 2, 2, device='cpu')
output_tensor = m(input_tensor)

