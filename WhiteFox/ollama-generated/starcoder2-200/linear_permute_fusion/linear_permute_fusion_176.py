
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4)

    def forward(self, x2):
        v1 = torch.nn.functional.linear(x2, self.linear1.weight, self.linear1.bias)
        v2 = v1.permute(0, 2, 1).float() # Permute the output tensor from the linear transformation.
        return v2


# Initializing the model