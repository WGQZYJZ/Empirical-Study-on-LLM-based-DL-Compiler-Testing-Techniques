
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.functional.conv2d(...)  # Use the functional API instead of nn module API here to test optimization
        bn = torch.nn.functional.batch_norm(...)
        output = bn(conv(x1))
        return output
# Input to the model
input_tensor = torch.randn(1, 1, 3, 28, 28)
