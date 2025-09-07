
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        output = torch.nn.functional.conv2d(input_tensor, weight)

        bn = torch.nn.BatchNormXd(...)
        output = bn(output)

        return output

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 4, 4)
