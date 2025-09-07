
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.functional.conv2d(...)
        bn = torch.nn.functional.batch_norm(...)
        output = conv + bn(x)
        return output

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 5, 7)
