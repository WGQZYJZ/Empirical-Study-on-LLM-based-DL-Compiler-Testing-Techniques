
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5, training=True) # Training mode
        v2 = torch.rand_like(x1, requires_grad=False)                # Not trainable tensor
        return self.linear(v1) + v2


# Initializing the model and setting fallback to true for random operations
m  = Model()
gm.set_fallback('random', True)

# Inputs to the model
x1 = torch.randn(1, 2, 2)
