
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
 
    def forward(self, x1):
        split_sizes = [x1.size(0), x1.size(0)]
        concatenated_tensor = torch.cat([self.conv1(split_tensors[0]), self.conv2(split_tensors[1])], dim=1)
        return self.conv1(concatenated_tensor)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
