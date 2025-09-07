
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)

        # Add another tensor
        v2 = v1 + other

        # Apply ReLU activation function to the result of adding two tensors 
        v3 = torch.relu(v2)

        return v3


# Initializing the model
m  = Model()
other  = torch.randn_like(torch.ones((8,)))


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
