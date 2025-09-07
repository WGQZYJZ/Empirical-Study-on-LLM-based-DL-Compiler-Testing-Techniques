
class ResidualModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, skip_x2):
        v1 = self.skip_connection(x1)  # Apply the Skip Connection function to the input tensor
        out = torch.cat((v1, skip_x2), dim=1)  # Add the Skip Connection with skip_x2 to it

        v2 = conv_transpose(out)  # Apply pointwise transposed convolution
        return torch.sigmoid(v2)


# Initializing the model
m = ResidualModel()


