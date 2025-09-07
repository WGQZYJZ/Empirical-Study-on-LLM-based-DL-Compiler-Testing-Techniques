
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        return torch.mm(x1, x2) + torch.eye(x1.shape[0])  # The result of the two matrix multiplications is added together

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 8, 8)
x2 = torch.randn(4, 3, 8, 8)
