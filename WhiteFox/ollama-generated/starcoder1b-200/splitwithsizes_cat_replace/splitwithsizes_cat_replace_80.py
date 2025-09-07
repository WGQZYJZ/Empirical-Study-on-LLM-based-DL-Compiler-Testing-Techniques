
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [64, 32]
        concatenated_tensor = torch.cat([torch.split(x1, split_sizes, dim)[i] for i in range(len(split_sizes))], dim)
        return torch.erf(concatenated_tensor)

# Initializing the model
m = Model()

