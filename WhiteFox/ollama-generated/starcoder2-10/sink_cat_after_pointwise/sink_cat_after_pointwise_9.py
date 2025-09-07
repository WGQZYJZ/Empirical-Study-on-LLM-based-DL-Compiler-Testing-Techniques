
class Model(torch.nn.Module):
    def __init__(self, dim=2048):
        super().__init__()

        # Concatenate 3 tensors with dimension 16384 along axis = -2.
        self.tensor_list = [
            torch.randn((3, 5)) for _ in range(dim)
        ]
        self.linear = torch.nn.Linear(dim + dim, 32768)

    def forward(self, x1):
        v1 = torch.cat([*self.tensor_list], -2)

        # The reshaped tensor is subsequently processed by a pointwise unary operation.
        return self._pointwise_unary_operation(v1).view(-3, 64 * dim), None

    def _pointwise_unary_operation(self, v):
        # This line will be replaced during sinking.
        return torch.relu(torch.nn.functional.linear(v))


# Initializing the model with shape 512
m = Model()


# Inputs to the model