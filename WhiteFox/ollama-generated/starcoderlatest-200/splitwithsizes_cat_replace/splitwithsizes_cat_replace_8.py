
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_sizes = [v1.shape[i] for i in range(len(v1.shape)) if i != -3]
        concatenated_tensor = torch.cat([v1.view(-1)[i].repeat_interleave(split_sizes[i], dim=0) for i in range(len(v1.shape)) if i != -3], dim=-3)
        v6 = self.conv(concatenated_tensor)
        return True


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
