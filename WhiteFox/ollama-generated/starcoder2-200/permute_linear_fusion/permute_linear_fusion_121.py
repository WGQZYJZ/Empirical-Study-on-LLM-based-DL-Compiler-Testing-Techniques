
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 3, 4, 1, 5, 6) # Permute the input tensor by specifying the permute indices
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(30, 87645, 94624, 2333343, 23, 4) # Create a 5 dimensional input tensor of shape (30 x 87645 x 94624 x 2333343 x 23 x 4).

