
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 8, kernel_size=3)

    def forward(self, x):
        v1 = x.view(-1, *x.shape[-3:])
        v2 = torch.nn.functional.relu(torch.nn.functional.max_pool2d(self.conv1(v1), (3)))
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1, *input_shape)
