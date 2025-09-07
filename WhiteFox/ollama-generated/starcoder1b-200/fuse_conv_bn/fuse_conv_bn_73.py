
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, conv, bn):
        v1 = x1.permute(0, 2, 1)
        output = bn(conv(input_tensor))  # Apply the batch normalization layer to the convolution output, and then rearrange it to a format that is compatible with the `torch.nn.functional` API.
        return output


# Initializing the model
m = Model()
