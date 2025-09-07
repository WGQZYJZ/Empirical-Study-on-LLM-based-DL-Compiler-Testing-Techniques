
class Model(torch.nn.Module):
    def __init__(self, mat1):
        super().__init__()
 
        self.mat1  = torch.nn.Parameter(mat1)
 
    def forward(self, x1):
        v1  = torch.addmm(x1, self.mat1[:, :], self.mat1[:, :])
        return torch.cat([v1, ], dim=-3)


# Initializing the model and setting hyperparameters
batch_size  = 20 # The batch size of the input tensors to the model
m  = Model(torch.randn((784, 784)))
 
# Inputs to the model
mat1  = torch.randn((batch_size,) + m.mat1.shape[1:]) # The first input tensor to the model
 
# Outputs from the model
y1 = m(mat1)

