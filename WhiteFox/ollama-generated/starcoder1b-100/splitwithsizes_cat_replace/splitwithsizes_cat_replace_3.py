
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [1]
        concatenated_tensor = torch.cat([self.conv(x1), self.conv(x1)], dim=split_sizes[0])  # Concatenate two convolutions into one tensor of shape (n1 * c1, n2 * c2)
        return True


# Initializing the model
m = Model()


