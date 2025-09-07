
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.5) # Apply dropout to the input tensor
        return t1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(32, 64, 87)
