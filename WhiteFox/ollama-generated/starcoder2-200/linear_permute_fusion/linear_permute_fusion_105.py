
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.linear(x1)  # Apply linear transformation to the input tensor
        return v.permute(*v.shape[::-1])


# Initializing the model
m  = Model()

# Inputs to the model
input_tensor  = torch.randn(2, 3).T

