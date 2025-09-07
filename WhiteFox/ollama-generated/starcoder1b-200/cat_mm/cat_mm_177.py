
class Model(torch.nn.Module):
    def __init__(self, dim=1024):
        super().__init__()
        self.fc = torch.nn.Linear(dim, 1)
 
    def forward(self, x1, x2):
        x3 = torch.cat([x1, x1], dim=-1)  # Concatenate the input tensors along the last dimension (batch size = 1).
        v1 = self.fc(x3)  # Apply a linear transformation to the concatenated input tensor.
        return v1


# Initializing the model
m = Model()


# Inputs to the model
input_tensor  = torch.randn(5, 1024)
__output__     = m(input_tensor, input_tensor)


