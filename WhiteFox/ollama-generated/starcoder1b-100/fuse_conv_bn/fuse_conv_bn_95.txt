
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x2 = torch.nn.functional.conv3d(input_tensor, self.linear.weight)  # The output of the conv3d function can be used as input to the batch normalization layer.

        bn = torch.nn.BatchNormXd(...)
        return bn(x2)


# Initializing the model
m = Model()


