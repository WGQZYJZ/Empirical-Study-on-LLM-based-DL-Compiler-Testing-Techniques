
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, self.linear1.weight, self.linear1.bias)

        #v4 = v3.permute()  # Permute the output tensor from the linear transformation.

        return v2


# Initializing the model
m = Model()


