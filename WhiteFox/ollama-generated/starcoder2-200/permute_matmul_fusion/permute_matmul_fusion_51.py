
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute((0, 2, 1))

        # Scenario 1: bmm or matmul of two tensors
        v3 = torch.bmm(v1, x2)

        return v3


# Initializing the model
m  = Model()


# Inputs to the model