
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()

        self.dim  = dim
        self.mat1  = torch.Tensor([[5., -3.], [-4., 7.]]) # 2x2 matrix for the first multiplication operation
        self.mat2  = torch.Tensor([[-8., 6.], [0, 9]])  # 2x2 matrix for the second multiplication operation
 
    def forward(self, x):
        v1  = torch.addmm(x, self.mat1, self.mat2)
        return torch.cat([v1], dim=self.dim)


# Initializing the model and its hyperparameter.
m  = Model(dim=0)
__dim__  = m.dim

# Input tensors for the model.
input_t1  = torch.Tensor([[5., -3.], [-4., 7.]]) # 2x2 matrix for the first multiplication operation
input_t2  = torch.Tensor([[-8., 6.], [0, 9]])   # 2x2 matrix for the second multiplication operation

