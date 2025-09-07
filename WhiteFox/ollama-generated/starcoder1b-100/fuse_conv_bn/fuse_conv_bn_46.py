
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv  = torch.nn.functional.conv2d(...)
        bn = torch.nn.functional.batch_norm(...)
        output = bn(conv(input_tensor))
        return output

# Initializing the model
m = Model()


