
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(input_tensor, self.linear.weight, self.linear.bias)
        v2 = x1.permute(...)  # Permute the output tensor from the linear transformation.
        return v2


# Initializing the model
m = Model()


