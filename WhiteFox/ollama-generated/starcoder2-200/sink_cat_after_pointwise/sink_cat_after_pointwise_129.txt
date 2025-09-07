
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Concatenate two tensors along dimension one and apply ReLU
        return torch.relu(torch.cat([x1, x1], dim=1))


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(32)

 __output__  = m(x1)

