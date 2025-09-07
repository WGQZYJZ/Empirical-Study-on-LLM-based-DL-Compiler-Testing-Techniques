
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(input_tensor=x1, ...)
        t2 = torch.rand_like(...)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 5)
