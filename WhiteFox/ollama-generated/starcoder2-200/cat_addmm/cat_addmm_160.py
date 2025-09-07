

class Model(torch.nn.Module):
    def __init__(self, mat1, mat2, input, dim):
        super().__init__()
        self.mat1 = mat1
        self.mat2 = mat2
        self.input = input
        self.dim = dim
 
    def forward(self, v3):
        v1  = torch.addmm(v3, self.mat1, self.mat2)
        return torch.cat([v1], self.dim)


# Initializing the model and the tensors required to run it on an input tensor of shape (N, D_out).
D = 50  # hidden layer size
D_in = 3  # input dimensionality
H = 2  # number of layers
N = 10  # batch size. Note that there should be more batches in the forward function! 
# (N, D) is (N, 3) times (3, 50). There should be N/batch_size matrices multiplied here to get a N/batch_size result. 
model = Model(torch.randn(D_in * H), torch.randn(H + 1) * D)
 
t2 = model.mat1 # random matrix t2. Should be of shape (3, 50). There should be a multiplication with the same shape here.
t4 = model.input.repeat(N, 1)# input, repeating each 50 elements N times to match the shape we are looking for.
t5 = torch.arange(H + 1) * D  # Shape of t5 is (2). This will be the sum along a dimension in our concatenation operation.
