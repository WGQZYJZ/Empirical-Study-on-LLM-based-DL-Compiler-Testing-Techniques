
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.5)
        t2 = torch.rand_like(t1, requires_grad=False) # No gradient is generated from the call to rand_like if the tensor has a different size than input_tensor.
        return x1 + t2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, requires_grad=True)
