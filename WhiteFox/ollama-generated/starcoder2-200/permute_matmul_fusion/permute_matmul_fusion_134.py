
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):

        v3  = x1.permute(0, 2, 1)
        v4  = torch.bmm(v3, x2)

        return v4

# Initializing the model
m  = Model()
__output__  = m(torch.randn(2, 5), torch.randn(2, 5))

