
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.cat([x1, x2], dim=0)
        v3  = v1.view(-1, x1.size()[-1]) # Reshape the concatenated tensor. The `-1` is an indication to the model.io module that the view method should be invoked on a dynamic value.
        return torch.nn.functional.relu(v3)

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(2, 3) # Tensor of shape (2, 3). The size of this tensor is statically fixed by the model.io module during the compilation process. Therefore, this tensor is constant throughout the model's forward method and we do not need to use a symbolic variable as an input argument.
x2 = torch.randn(20, 3) # Tensor of shape (20, 3). The size of this tensor is statically fixed by the model.io module during the compilation process. Therefore, this tensor is constant throughout the model's forward method and we do not need to use a symbolic variable as an input argument.

