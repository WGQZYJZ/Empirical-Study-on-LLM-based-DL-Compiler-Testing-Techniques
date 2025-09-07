
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.conv2 = torch.nn.ConvXd(...)  # X should match with ConvXd
        self.conv3 = torch.nn.ConvXd(...)  # X should match with ConvXd
        self.bn1 = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        self.bn2 = torch.nn.BatchNormXd(...)  # X should match with BatchNormXd
        self.bn3 = torch.nn.BatchNormXd(...)  # X should match with BatchNormXd
        self.linear1 = torch.nn.Linear(64, 64)

    def forward(self, x1):
        out = []
        for i in range(len(out)):
            conv_out = self.conv1(input_tensor[i])  # X can be 1, 2, or 3 representing the dimension
            bn_out = self.bn1(conv_out)
            linear_out = self.linear1(bn_out)
            out += [linear_out]
        out += [self.conv2(input_tensor)]
        out += [self.bn2(output[0])]
        return output


# Initializing the model
m = Model()


