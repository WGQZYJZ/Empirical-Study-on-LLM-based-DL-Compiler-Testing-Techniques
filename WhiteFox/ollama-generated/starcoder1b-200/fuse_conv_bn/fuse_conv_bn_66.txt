
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # The output of conv1 is input to the batch norm layer
        # The input of conv2 follows this pattern
        # A linear operation (x + w * y + b) follows this pattern
        # The weights and bias are initialized at random

        w = self.linear.weight
        b = self.linear.bias

        x_conv1 = torch.nn.functional.conv2d(x1, w, bias=b, stride=(2, 2), padding=0)
        x_bn1   = torch.nn.functional.batch_norm(x_conv1, 1.0, eps=1e-5)
        # A linear operation (x + b) follows this pattern

        y = x_bn1 + x_conv2
        return y


# Initializing the model
m = Model()


