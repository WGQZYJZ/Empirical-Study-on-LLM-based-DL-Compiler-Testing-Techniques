
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.functional.conv2d(...)  # X should match with input_tensor
        bn  = torch.nn.functional.batch_norm(...)  # Y must be a BN instance with the same running statistics as conv
        return bn(conv(input_tensor))


# Inputs to the model
x1 = ...
