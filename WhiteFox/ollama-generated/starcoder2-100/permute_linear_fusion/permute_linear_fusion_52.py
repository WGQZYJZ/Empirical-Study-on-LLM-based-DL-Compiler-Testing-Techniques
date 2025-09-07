
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1) # Permute the input tensor
        return torch.nn.functional.linear(v1, torch.nn.Linear(3).weight + 5)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)

