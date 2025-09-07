
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         return torch.nn.functional.dropout(x1, 0.5), randlike(x1)


# Initializing the model and inputs
m = Model()
x1 = torch.randn(2)

