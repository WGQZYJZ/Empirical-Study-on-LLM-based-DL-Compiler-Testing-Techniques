
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1, p=0.5)
        v2  = torch.nn.functional.dropout(v1, p=0.3, training=False)
        v3  = torch.nn.functional.linear(v2, self.linear.weight, self.linear.bias)

        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 5)
