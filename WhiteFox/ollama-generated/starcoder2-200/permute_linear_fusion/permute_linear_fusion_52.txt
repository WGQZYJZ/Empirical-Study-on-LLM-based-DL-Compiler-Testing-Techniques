
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor (3D to 4D)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)

        v3 = v2[..., -1:]  # Slice the last dimension of the output tensor
        return v3

# Initializing the model