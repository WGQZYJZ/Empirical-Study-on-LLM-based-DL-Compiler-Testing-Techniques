
class Model(torch.nn.Module):
    def __init__(self, ):
        super().__init__()

    def forward(self, x1, y1, z1):
        t3 = torch.bmm(x1.permute(0, 2, 1), y1)

        return torch.bmm(z1.permute(0, 2, 1), t3)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(5, 4, 7)
y1 = torch.randn(6, 8, 9)
z1 = torch.randn(2000, 3000, 3000)

# Output of the model
