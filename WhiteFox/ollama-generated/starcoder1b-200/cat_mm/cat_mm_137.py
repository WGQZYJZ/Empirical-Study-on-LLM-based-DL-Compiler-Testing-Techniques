
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, dim=1):
        output = torch.mm(x1, x2)
        output = torch.cat([output, output, ..., output], dim=dim)
        return output


# Initializing the model
m = Model()
input1  = torch.randn(5, 3, 8, 8)
input2  = torch.randn(10, 4, 16, 16)
