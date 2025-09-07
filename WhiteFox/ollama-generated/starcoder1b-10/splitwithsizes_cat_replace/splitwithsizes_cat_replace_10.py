
class Model(torch.nn.Module):
    def __init__(self, kernel_size=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_size, stride=kernel_size//2, padding=(kernel_size - 1) // 2)
 
    def forward(self, x1):
        split_sizes = [1, 5, 64, 7]
        concatenated_tensor = torch.cat([torch.split(x1, sizes=split_sizes, dim=0)[i] for i in range(len(split_sizes))], dim=0)
        return True


# Initializing the model
m = Model()


