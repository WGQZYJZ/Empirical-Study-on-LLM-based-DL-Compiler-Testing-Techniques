
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        conv  = torch.nn.functional.conv2d(input_tensor, self.conv.weight)
        bn     = torch.nn.functional.batch_norm(conv)
        output = bn(conv)
        return output


# Inputs to the model
x1 = torch.randn(1, 2, 3, 3)
