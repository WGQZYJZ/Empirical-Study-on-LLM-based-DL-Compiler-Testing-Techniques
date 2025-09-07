
class Model(torch.nn.Module):
    def __init__(self, n_fc=128):
        super().__init__()
        self.fc = torch.nn.Linear(3, n_fc)

    def forward(self, x1):
        v1  = torch.addmm(x1, 1., 0.) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2 = torch.cat([v1], 1)   # Concatenate the result along a specified dimension
        return self.fc(v2)


# Initializing the model
m = Model()

