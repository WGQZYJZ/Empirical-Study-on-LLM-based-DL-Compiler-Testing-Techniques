
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension of the input tensor
        self.bn1 = torch.nn.BatchNormXd(...)
        self.conv2 = torch.nn.ConvXd(...)  # X should match with ConvXd
        self.bn2 = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)  # Permute the input tensor

        v2 = torch.nn.functional.convXd(
            x=v1,
            weight=self.conv1.weight,
            bias=self.conv1.bias
        )  # X should match with ConvXd
        bn_out = self.bn1(v2)  # Run the batch normalization on v2

        v3 = torch.nn.functional.batch_norm(
            x=v2,
            weight=self.bn1.weight,
            bias=self.bn1.bias
        )  # X should match with ConvXd
        bn_out = self.bn2(v3)  # Run the batch normalization on v3

        output = bn_out  # Return the original bn_out as the output
        return output


# Initializing the model
m = Model()


