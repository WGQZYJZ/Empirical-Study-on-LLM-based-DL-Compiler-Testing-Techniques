
class Model(torch.nn.Module):
    def __init__(self, mat1: torch.Tensor = None, mat2: torch.Tensor  = None, dim: int  = None) -> None:
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
        if isinstance(mat1, torch.Tensor):
            self.mat1  = mat1

        if isinstance(mat2, torch.Tensor):
            self.mat2  = mat2
 
        if dim is not None: 
            self.dim  = dim
 
    def forward(self, x1: torch.Tensor) -> torch.Tensor:
        v1  = torch.addmm(x1, self.mat1, self.mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2  = torch.cat([v1], dim=self.dim) # Concatenate the result along a specified dimension
        return v2


# Initializing the model with custom tensors and an integer for concatenation
m = Model(mat1, mat2, dim).to_onnx()

# Inputs to the model in dictionary format
__input__  = {'x1': torch.randn(32, 5, 480, 64)}

