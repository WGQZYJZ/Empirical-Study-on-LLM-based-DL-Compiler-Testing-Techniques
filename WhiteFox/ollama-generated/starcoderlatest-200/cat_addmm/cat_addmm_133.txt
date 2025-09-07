
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.fc = torch.nn.Linear(8, 24)
        self.conv = torch.nn.Conv1d(3, 256, kernel_size=(1,), stride=(1,))
        self.bn1 = torch.nn.BatchNorm2d(1, affine=False)
        self.pool = torch.nn.MaxPool1d(2, stride=2)
 
    def forward(self, x1):
        v1  = self.fc(x1)
        t1  = torch.addmm(v1, mat1, mat2) # Add the matrix multiplication of two tensors to an input tensor
        v4  = self.conv(t1)
        v5  = self.bn1(v4)
        t2  = self.pool(v5)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x_batch = torch.randn(batch, 3, length, d)
