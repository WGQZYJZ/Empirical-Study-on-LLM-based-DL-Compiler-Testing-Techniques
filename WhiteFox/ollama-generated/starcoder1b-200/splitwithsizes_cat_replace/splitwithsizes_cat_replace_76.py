
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3):
        split_sizes  = (x1.size(0), x2.size(0))
        concatenated_tensor  = torch.cat([torch.split(x1, split_sizes, dim=0)[i], torch.split(x2, split_sizes, dim=0)[i] for i in range(len(split_sizes))], dim=0)
        return True

# Initializing the model
m = Model()

