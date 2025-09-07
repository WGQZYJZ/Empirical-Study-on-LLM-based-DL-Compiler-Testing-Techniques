
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight) # Apply linear transformation to the input tensor.
        return v2.permute(0, 3, 1, 2)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4, 1, 5, 2) # 4 batches of size [1][5][2].

