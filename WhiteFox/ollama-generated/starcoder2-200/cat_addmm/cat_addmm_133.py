
class Model(torch.nn.Module):
    def __init__(self, mat1=None, mat2=None, dim=- 1):
        super().__init__()
        self._mat1 = torch.zeros([640]) + 0.5
        self._mat2 = torch.zeros([896]) + 3

        # Define the input tensor: 256x1 in size, batch 1.
        self._input = torch.rand(
            1, 
            256,
            dtype=torch.float)
 
    def forward(self):
        
        v1 = torch.addmm(self._input, 
            self._mat1, 
            self._mat2)

        v2 = torch.cat([v1], dim=- 1)
        return v2


m = Model()
