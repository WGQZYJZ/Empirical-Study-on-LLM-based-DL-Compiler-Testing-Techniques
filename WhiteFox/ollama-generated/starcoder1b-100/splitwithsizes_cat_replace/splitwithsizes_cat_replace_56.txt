
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [3, 4]
        concatenated_tensor = torch.cat([torch.split(x1, split_sizes, dim)[i] for i in range(len(split_sizes))], dim)
        return True if len(concatenated_tensor.shape) == 2 and len(set(concatenated_tensor.shape).symmetric_difference({0})) == 0 else False


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
