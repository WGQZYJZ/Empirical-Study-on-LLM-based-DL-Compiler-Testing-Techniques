
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0) # concat tensor along the first dimension
        v2 = v1.view(-1)  # reshape tensor to a vector of shape [n] (Note: we are not reshaping the last dimension)
        v3 = self.relu(v2)  # apply a pointwise operation on the reshaped tensor
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 2)
x2 = torch.randn(4, 6)
