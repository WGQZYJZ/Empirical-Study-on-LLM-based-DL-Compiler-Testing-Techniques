
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v1 = self.conv(x1).matmul(torch.eye(4))
        # Concatenate the result along a specified dimension
        return torch.cat([v1], dim=1)


# Initializing the model
m = Model()


