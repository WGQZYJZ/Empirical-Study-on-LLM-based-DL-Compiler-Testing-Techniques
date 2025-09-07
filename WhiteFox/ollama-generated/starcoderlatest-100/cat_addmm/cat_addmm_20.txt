
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(64*64, 1024)
 
    def forward(self, x1):
        v1 = torch.addmm(x1.view(-1, 64 * 64), mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2 = torch.cat([v1], dim=0) # Concatenate the result along the specified dimension
        return self.fc1(v2)


# Initializing the model
m = Model()

