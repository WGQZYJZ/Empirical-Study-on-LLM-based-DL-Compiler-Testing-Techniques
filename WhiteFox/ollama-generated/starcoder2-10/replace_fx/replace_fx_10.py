
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.nn.functional.linear(x1, self.linear.weight) # Apply linear transformation to the permuted tensor.
        v3 = torch.nn.functional.dropout(v2, p=0.5, training=True)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4,)

