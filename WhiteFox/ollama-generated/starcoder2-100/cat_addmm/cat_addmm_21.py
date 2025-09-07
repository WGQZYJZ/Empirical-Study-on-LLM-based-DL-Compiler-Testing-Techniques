
class Model(torch.nn.Module):
    def __init__(self, dim1=0):
        super().__init__()
 
        # Initializing the matrix multiplication operation along each batch dimension of the input tensor
        self.m_input = torch.zeros((8, 3))
 
    def forward(self, x1):
 
        # Performing a matrix multiplication with both tensors and concatenating them on axis 0
        v1  = torch.addmm(x1[None].expand(-1, -1), m1[None], m2[None]).squeeze()  # Here we expand the input and matrices to match the required dimensions of addmm
 
 
    def concat_op(self):
        return torch.cat([t1], dim=0)
 
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 56, 48) # The first tensor in our input to the model (shape: 2 x 3 x 56 x 48). We assume that we need two of these tensors as input to this model, and we can concatenate them along the batch dimension.
