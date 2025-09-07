
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.25, training=self.training)
        v2 = torch.rand_like(v1, 1.0/32)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 4, 8, requires_grad=True)
