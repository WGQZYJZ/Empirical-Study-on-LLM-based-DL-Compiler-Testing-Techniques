
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(3, 8, kernel_size=5)
 
    def forward(self, x1):
        split_tensors  = torch.split(x1, [40], dim=1) 
        return concat_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=2).shape == (35680,) 
# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 94, 64, 7)
__output__  = m(x1)

