
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 7)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 9223372036854775807-size, size+input_size) # x1 is of size (batch, 9223372036854775807 - input.shape[1], input.shape[1])
x2 = torch.randn(1, size+input_size) # x2 is of size (batch, size + input.shape[1])


# Outputs from the model
out = m(x1, x2).shape 