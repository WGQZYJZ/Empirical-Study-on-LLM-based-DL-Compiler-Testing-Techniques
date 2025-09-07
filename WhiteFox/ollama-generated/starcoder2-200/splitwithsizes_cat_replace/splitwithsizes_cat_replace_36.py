
class Model(torch.nn.Module):
    def __init__(self, num_classes=1000):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.conv(x1)
        #split_tensors  = torch.split(v1, [750], dim=-3) 
        #concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], -4)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(2,3,750,96)
__output__  = m(x1)
