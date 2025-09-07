
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1, x2):  # Takes two input tensors as parameters
        v1 = torch.addmm(x1, self.mat1, self.mat2)  
        v2 = torch.cat([v1], dim)
        return v2
    
# Initializing the model and its input tensor
m = Model()
m.load_state_dict({'mat1': torch.randn(500, 3), 'mat2': torch.randn(3, 7)})
x1  = torch.randn(4) # A random input vector of length 4 with shape (4,)
x2  = torch.randn(98, 6) # A 98 x 6 matrix to be concatenated with v1
__output__  = m(x1, x2)

