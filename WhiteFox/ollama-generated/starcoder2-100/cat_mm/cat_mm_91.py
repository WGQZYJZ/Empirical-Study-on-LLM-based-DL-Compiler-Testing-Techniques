
class Model(torch.nn.Module):
    def __init__(self, dim=32):
        super().__init__()

        self.weight = torch.nn.Parameter(
            torch.zeros((dim + 1,), dtype=torch.float)
        )
 
    def forward(self, x):
        v1  = torch.matmul(x, self.weight[:-1]) # Matrix multiplication of two tensors
        v2  = v1.clamp(-50, 50) # Clamp the output of matrix multiplication between -50 and +50
        v3  = v2.reshape((-1,) + tuple((v2.shape[-3:] // dim) * (dim + 1)))  # Reshape the clamped matrix multiplication result to a tensor of a specified shape

        v4  = torch.nn.functional.pad(
            v3, 
            pad=(0, 0),
            mode='constant',
        )  # Pad the clamped matrix multiplication result
        
        return v4

# Initializing the model
m1  = Model()
m2  = Model(dim=8)

