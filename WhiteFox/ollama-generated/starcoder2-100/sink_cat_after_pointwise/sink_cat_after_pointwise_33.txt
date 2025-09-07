
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        # Concatenate 3 tensors along 0-th dimension, and apply pointwise unary operation to the result.
        t2 = torch.cat([x1[...], x1[...], x1[...]], dim=...)
        t4  = torch.relu(t2.view(-1))

# Initializing the model
m = Model()


# Inputs to the model:
__output__  = m(torch.randn(3, 5, 3))

