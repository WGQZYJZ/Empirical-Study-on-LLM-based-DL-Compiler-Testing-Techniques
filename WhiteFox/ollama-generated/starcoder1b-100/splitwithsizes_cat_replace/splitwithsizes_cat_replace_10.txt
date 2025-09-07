
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        split_sizes = [4, 4]
        concatenated_tensor = torch.cat([self.conv1(x1[i]) for i in range(len(split_sizes))], dim=2)  # Concatenate the split tensors along the same dimension
        v1 = self.conv1(x1)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 3, 64, 64)
__output__  = m(x1)

