
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)

    def forward(self, x):
        conv = self.conv(x) # Fuse 2 convolution layers with the output tensor of `forward` as the input
        bn = torch.nn.functional.batch_norm(input=conv, eps=0.001, momentum=0.1)
        return bn


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 3, 6)
