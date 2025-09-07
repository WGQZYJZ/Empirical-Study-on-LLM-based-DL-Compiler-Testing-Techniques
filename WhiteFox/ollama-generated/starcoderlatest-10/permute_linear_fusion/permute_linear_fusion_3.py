
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = torch.squeeze(x1.permute(0, 2, 1), axis=[1]) # Remove the last dimension of input tensor
        v2 = torch.add(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 4)
