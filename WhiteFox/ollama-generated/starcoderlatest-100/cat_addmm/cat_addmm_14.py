
class Model(torch.nn.Module):
    def __init__(self, n_classes=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc1 = torch.nn.Linear(8, 64) # number of output channels is 64
        self.fc2 = torch.nn.Linear(64, n_classes)
 
    def forward(self, x):
        t1 = torch.addmm(x, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2 = torch.cat([t1], dim) # Concatenate the result along a specified dimension
        v1  = F.relu(self.fc1(F.relu(self.conv(x))))
        v2  = self.fc2(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
input = torch.randn(batch_size, input_dim)
