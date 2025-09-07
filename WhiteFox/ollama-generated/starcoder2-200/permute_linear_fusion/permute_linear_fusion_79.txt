
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1) # Permute the input tensor (swap dim 2 and 1 in the shape of [1x4x5])

        return torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)


# Initializing the model