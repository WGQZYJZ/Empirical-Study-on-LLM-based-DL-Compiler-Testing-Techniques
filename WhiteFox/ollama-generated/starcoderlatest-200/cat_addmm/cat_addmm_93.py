
class Model(torch.nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=(5, 5))
        self.fc = torch.nn.Linear(8 * 56 * 56, num_classes)
 
    def forward(self, x):
        t1 = torch.addmm(x, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2 = torch.cat([t1], dim=1)  # Concatenate the result along dimension 1
        return self.fc(t2.view(t2.shape[0], -1))

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 3, 64, 64)
