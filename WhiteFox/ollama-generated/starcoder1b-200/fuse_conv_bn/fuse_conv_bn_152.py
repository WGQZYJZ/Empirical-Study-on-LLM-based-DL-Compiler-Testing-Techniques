
class Model(torch.nn.Module):
    def __init__(self, num_features):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        self.conv   = torch.nn.ConvXd(...)
        self.bn     = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        conv_output  = self.conv(v1)
        bn_output    = self.bn(conv_output)
        output = bn_output.matmul(self.linear.weight).view(-1, self.linear.out_features)
        return output


# Initializing the model
m = Model(2)

