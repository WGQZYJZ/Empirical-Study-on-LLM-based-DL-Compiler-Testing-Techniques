
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = x1.permute(0, 3, 1, 2) # Permute the input tensor. The last two dimensions swap their places.
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) # Apply linear transformation to the permuted tensors with swapped dimensions.
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 2 , 2)
