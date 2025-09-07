
class Model(torch.nn.Module):
    def __init__(self, d1=8, stride=2, p=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, d1, kernel_size=1, stride=stride, padding=p)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_tensors = torch.split(v1, split_sizes=(1,), dim=1)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim) 
        return concatenated_tensor


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
