
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.bmm(x1, x2)  # input tensor A and B are permuted tensors.
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 3, 3, requires_grad=True)
x2 = torch.randn(3, 4, 3, requires_grad=True)
