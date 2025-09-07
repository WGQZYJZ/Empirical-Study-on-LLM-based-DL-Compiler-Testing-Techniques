
class Model(torch.nn.Module):
    def __init__(self, x_size=32, h_size=100):
        super().__init__()
        self.fc1 = torch.nn.Linear(x_size, h_size)

    def forward(self, x1):
        v1 = torch.addmm(x1, x1, x1)  # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2 = torch.cat([v1], dim=0)  # Concatenate the result along a specified dimension
        v3 = self.fc1(v2)  # Forward propagate the output of the linear transformation
        return v3


# Initializing the model
m = Model()


