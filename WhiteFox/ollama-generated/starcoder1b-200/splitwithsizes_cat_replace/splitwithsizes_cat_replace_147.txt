
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_sizes = torch.tensor([64, 57, 51], dtype=torch.long).view(1, 3, 1, 1) # split sizes in the input tensor
        concatenated_tensor = torch.cat([
            torch.split(v1, split_sizes[0], dim=1)[0], 
            torch.split(v1, split_sizes[1], dim=1)[1],
            torch.split(v1, split_sizes[2], dim=1)[2]
        ], dim=1)  # concatenate along the second dimension
        return concatenated_tensor


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
