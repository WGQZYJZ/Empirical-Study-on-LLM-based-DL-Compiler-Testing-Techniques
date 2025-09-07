
class Model(torch.nn.Module):
    def __init__(self, x1 = None, y2 = None, y3 = None, z4 = None):
        super().__init__()
        self._input1  = torch.nn.Parameter(x1) if x1 is not None else [] 
        self._input2  = torch.nn.Parameter(y2) if y2 is not None else []
        self._input3  = torch.nn.Parameter(z4) if z4 is not None else []
        self._input4  = torch.nn.Parameter(z4) if z4 is not None else []
 
    def forward(self, t1):        
        v0_1  = torch.nn.functional.mm(t1[self._input1], self._input2) # Matrix multiplication between input1 and input2
        v0_3  = v0_1 * 8.596470293535057 # Multiply the results of the matrix multiplication by another constant 
        v0_4  = torch.nn.functional.mm(t1[self._input3], self._input4) # Matrix multiplication between input3 and input4
        v0_5  = t1 * (v0_1 + v0_2) # Add the results of two matrix multiplications together, multiply them with the output of the first convolution, and then add to the output tensor
        return [v0_5]

m = Model(x1=x1, y2=y2, z4=z3, z4=z4)

