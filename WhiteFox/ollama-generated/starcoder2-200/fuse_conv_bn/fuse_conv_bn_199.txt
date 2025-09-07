
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 2)

    def forward(self, x1):
        v1 = x1.permute([0, 3, 1]) # Permuting dimensions to match the input tensor
        v2 = torch.nn.functional.conv_transpose3d(v1, self.linear.weight, self.linear.bias)

        return v2

# Initializing the model