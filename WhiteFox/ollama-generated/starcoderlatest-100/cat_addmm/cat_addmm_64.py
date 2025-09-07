
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        mat1 = torch.randn(5, 4, 4, 3).permute(0, 1, 3, 2, 4)
        mat2 = torch.randn(8, 4, 1, 3)
        t1 = torch.addmm(x1, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2 = torch.cat([t1], dim=1) # Concatenate the result along dimension dim (1 here is for 1st dimension i.e., channel)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 5, 64, 64)
