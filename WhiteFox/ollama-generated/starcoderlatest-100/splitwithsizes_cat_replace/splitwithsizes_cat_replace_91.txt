
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        s_x1 = torch.split(input_tensor, split_sizes, dim)
        c_x1 = torch.cat([s_x1[i] for i in range(len(split_sizes))], dim)
        return c_x1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
