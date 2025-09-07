
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [3, 4]
        concatenated_tensor = torch.cat([
            torch.split(x1, split_sizes[0], dim=1)[0],
            torch.split(x1, split_sizes[1], dim=1)[1]])
        return concatenated_tensor


# Initializing the model
m = Model()


