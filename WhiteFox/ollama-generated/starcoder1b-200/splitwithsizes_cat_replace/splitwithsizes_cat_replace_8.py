
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [2, 4]
        concatenated_tensor = torch.cat([
            self.conv(x), self.conv(x1) for x in
            torch.split(x1, split_sizes, dim=-2)  # Split x into several tensors along -2 and concatenate them along -1
        ])
        return concatenated_tensor


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
y1  = torch.cat([
    self.conv(x) for x in torch.split(x1, [2, 5], dim=-2)  # Split x into several tensors along -2 and concatenate them along -1
])
__output__  = m(y1)

