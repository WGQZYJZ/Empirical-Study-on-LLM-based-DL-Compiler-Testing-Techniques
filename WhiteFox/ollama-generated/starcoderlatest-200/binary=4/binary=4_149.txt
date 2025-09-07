
class Model(torch.nn.Module):
    def __init__(self, other_tensor: torch.Tensor = None):
        super().__init__()
        self.linear = torch.nn.Linear(8, 3)
 
        # If `other_tensor` is specified, set this as the first linear layer's second input, otherwise leave it unspecified
        if other_tensor is not None:
            self.conv1 = torch.nn.Conv2d(3, 64, 3, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
 
        # If `other_tensor` is specified as an input of this layer, set it as the second linear layer's first input
        if other_tensor is not None:
            v3 = self.conv1(v2)
        else:
            v3 = v2

        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
