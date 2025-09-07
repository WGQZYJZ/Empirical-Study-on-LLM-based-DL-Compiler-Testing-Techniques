
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # Use `ConvXd` and `BatchNormXd` functions here
        conv = torch.nn.functional.convXd(...)
        bn  = torch.nn.functional.batch_norm(...)
        output = bn(conv(input_tensor))
        return output


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 2, 2)
