
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, (2, 2))

    def forward(self, x1):
        conv_output = F.conv2d(x1, self.conv.weight)
        return F.batch_norm(conv_output, weight=self.bn.weight, bias=self.bn.bias, running_mean=self.running_mean, running_var=self.running_var, momentum=0.1, eps=1e-3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 28, 28)
