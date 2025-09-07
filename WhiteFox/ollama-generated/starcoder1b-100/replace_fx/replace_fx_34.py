
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return 0.5 * (torch.tensor(2., requires_grad=True) + torch.rand_like(x1, requires_grad=False))


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(4, 3, 3) # The input tensor has 4 dimensions, and each dimension has three elements (the shape [batch_size, num_inputs, ...]).
