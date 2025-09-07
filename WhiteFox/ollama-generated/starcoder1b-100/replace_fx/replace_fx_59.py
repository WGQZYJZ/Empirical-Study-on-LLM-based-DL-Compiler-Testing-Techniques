
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Apply dropout to the input tensor and generate a random tensor with same size as the input_tensor
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear(v1)

        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
