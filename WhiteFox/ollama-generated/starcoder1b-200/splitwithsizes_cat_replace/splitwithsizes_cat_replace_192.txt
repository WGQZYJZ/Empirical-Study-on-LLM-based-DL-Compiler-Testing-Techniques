
class Model(torch.nn.Module):
    def __init__(self, n_layers, stride=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=1, stride=stride, padding=1)
 
    def forward(self, x1):
        split_sizes = [torch.tensor([n + 1]).type(x1.dtype).to(x1.device) for n in range(self.n_layers)]
        concatenated_tensor = torch.cat(
            [torch.split(x1, n, dim=dim) for i, n in enumerate(split_sizes) for dim in range(i + 1)],
            dim=0
        )
        output = self.conv(concatenated_tensor)
        return output


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
