
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.tensor([0, 1, 2], dtype=torch.float32) # mat1 is a matrix with three elements in the first row and one element in the third row
        self.mat2 = torch.tensor([4, 5, 6], dtype=torch.float32) # mat2 is a matrix with two elements in the second row
    def forward(self, input):
        v1 = torch.addmm(input, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim=1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
