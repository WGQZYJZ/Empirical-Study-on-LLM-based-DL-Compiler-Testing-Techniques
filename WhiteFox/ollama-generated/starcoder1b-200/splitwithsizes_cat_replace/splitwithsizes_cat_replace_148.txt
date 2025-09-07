
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [torch.tensor([4]), torch.tensor([5])]
        concatenated_tensor = torch.cat([torch.split(x1, split_sizes[0], dim), torch.split(x1, split_sizes[1], dim)], dim)
        return self.conv(concatenated_tensor)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
