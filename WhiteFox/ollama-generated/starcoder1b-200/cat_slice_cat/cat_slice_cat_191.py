
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        t1  = torch.cat([x1, x1], dim=1) # Concatenate the original input and original input along dimension 1
        t2  = t1[:, :size]   # Slice the concatenated tensor along dimension 1
        t3  = t2[: size - 10 : 11] # Further slice the tensor along dimension 1
        t4  = torch.cat([t1, t3], dim=1) # Concatenate the original input and the sliced tensor along dimension 1
        return t4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 1, 64, 64)
