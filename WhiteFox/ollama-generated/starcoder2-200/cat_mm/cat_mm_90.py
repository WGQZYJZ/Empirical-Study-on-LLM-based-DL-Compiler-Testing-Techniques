class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1):  # pylint: disable=arguments-differ
        v1 = torch.mm(t1[:, :3], t1[:, 3:])  # Matrix multiplication of two input tensors
        v2 = torch.cat([v1] * len(t1))  # Concatenation of the result tensor along a specified dimension
        return v2


# Initializing the model
m = Model()


# Inputs to the model
t1 = torch.randperm((50, 6), out=torch.empty((3780,), dtype=torch.int))
