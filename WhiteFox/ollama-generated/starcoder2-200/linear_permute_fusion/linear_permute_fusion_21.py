
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias) # linear transformation 0

        v2 = v1.permute(...) # permute on the linear transformation output tensor (v1)
        return v2


# Initializing the model