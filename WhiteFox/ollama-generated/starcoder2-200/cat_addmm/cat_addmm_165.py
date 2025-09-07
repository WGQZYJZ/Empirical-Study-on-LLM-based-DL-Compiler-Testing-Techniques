
class Model(torch.nn.Module):
    def __init__(self, in_features1: int = 50) -> None:
        super().__init__()
 
        self.fc1 = torch.nn.Linear(in_features1, num_classes=8)
 
    def forward(self, x1):
        
        v2 = torch.cat([torch.addmm(x1, mat1, mat2)], dim=0)
        return v2
 
# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3,50) # The number of rows must be higher than or equal to 1 and lower than or equal to the batch size (number of examples). The number of columns in both the mat1 tensor and the mat2 tensor must match each other.
mat1 = torch.randn(50,47386) # The number of rows must be higher than or equal to 1 and lower than or equal to num_rows * num_cols / batch size (number of examples). 
                              # The number of columns in mat2 must match the number of columns in input.
mat2 = torch.randn(50,3794)

 __output__=m(x1)
