
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # TODO: generate an input tensor for this model
        split_sizes = [1]

        with torch.no_grad():
            v1 = self.conv1(x1)
            v2 = self.conv2(v1)
            v3 = self.conv3(v2)
            v4 = self.conv4(v3)
            v5 = self.conv5(v4)
            v6 = self.conv6(v5)

        return True


# Initializing the model
m = Model()

