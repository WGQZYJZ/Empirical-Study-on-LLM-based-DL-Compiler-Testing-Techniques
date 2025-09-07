
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
        self.dim = dim
        self.linear1  = torch.nn.Linear(832 * 496 + 65536, 7)
        self.linear2  = torch.nn.Linear(7 + 1 + 7, 10)
 
    def forward(self, x):
        t1  = torch.addmm(x, mat1, mat2) # Compute a matrix multiplication of matrices mat1 and mat2 and add the result to tensor x
        t2  = torch.cat([t1], dim=dim) 
        return t2


# Initializing the model
m  = Model()

# Inputs to the model
input_size  = [3, 832] + [-1, -1, -1] # Size of input tensor x should be [batch size x 832 x -1 x -1]. 
                                      # Please make sure that batch size equals 3. Otherwise, it will raise errors during execution time
mat1 = torch.randn(65536 + 7, 496)   # Size of matrix mat1 should be [65536+7 x 496].
                                      # Please make sure that the batch size in the first dimension of tensor input_size is set to 3. Otherwise, it will raise errors during execution time
mat2 = torch.randn(832 + 1 + 7, 1)    # Size of matrix mat2 should be [496 x 832+1+7].
                                      # Please make sure that the batch size in the first dimension of tensor input_size is set to 3. Otherwise, it will raise errors during execution time
dim = 0                                # dim is a constant which indicates the dimension along which the output tensor should be concatenated. It is a positive integer or negative integer.
                                       # Please make sure that batch size in the first dimension of tensor input_size is set to 3. Otherwise, it will raise errors during execution time
x = torch.randn(*input_size)            # The size of tensor x follows from the size of input tensor input_size. 
                                        # Therefore, we need to use dynamic shape to specify its size.

 