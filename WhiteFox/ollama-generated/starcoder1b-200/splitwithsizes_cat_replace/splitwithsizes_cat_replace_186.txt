
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [3, 4] # Dimension sizes along which the split and concatenation operations are performed
        concatenated_tensor = torch.cat([torch.split(x1, sizes, dim=0) for sizes in split_sizes], dim=0)
        return concatenated_tensor


# Initializing the model
m = Model()

