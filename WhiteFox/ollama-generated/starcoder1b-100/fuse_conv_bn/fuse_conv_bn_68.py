
class FusedBatchNorm(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input):
        return torch.autograd.Function.conv2d(
            input, weight=input.new_zeros(*input.size()), bias=input.new_zeros(*input.size()),
            stride=1, padding=0)

    @staticmethod
    def backward(ctx, grad_output):
        return None

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn    = FusedBatchNorm()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.conv(v1)
        bn_output = self.bn(v2)
        v3 = torch.nn.functional.linear(bn_output, self.linear.weight, self.linear.bias)
        return v3


# Inputs to the model
x1 = torch.randn(1, 2, 2)
