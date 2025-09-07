
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [64, 3]  # For a tensor x0 = 0.5 * x1 + 1.0, one could run torch.split([0.5 * x1 + 1.0], [32, 64])
        concatenated_tensor = torch.cat(torch.split(x1, split_sizes), dim=1)
        return concatenated_tensor

# Initializing the model
m = Model()


