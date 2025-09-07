
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv  = torch.nn.functional.conv_2d(...)  # X can be 1, 3 or 4 representing the dimension
        bn  = torch.nn.functional.batch_norm(...)  # X should match with ConvXd
        output = bn(conv(input_tensor))
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3, 4)
