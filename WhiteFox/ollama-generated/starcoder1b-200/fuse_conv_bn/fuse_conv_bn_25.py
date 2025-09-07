
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # No need to add 'input_tensor', it is already used by the optimizer in fuse_conv_bn()
        output = convXd(x1)
        return batch_normXd(output)

# Inputs to the model
x1  = torch.randn(1, 2, 2)
