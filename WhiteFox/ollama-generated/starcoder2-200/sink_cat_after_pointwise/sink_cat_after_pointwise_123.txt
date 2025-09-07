
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t3 = torch.relu(x1.view(-1))  # Apply ReLU to the reshaped tensor.
        return t3


m = Model()

x1 = torch.randn(4)


__output__  = m(x1)

# Inputs to the model
x1 = torch.randn(2, 2)
