
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1) 
        v2  = v1 *  0.5       
        v3  =  v1  *    v1      *        v1       
        v4  = v3  *    0.044715  
        v5  =v1 +v4
        v6  = v5 *    0.7978845608028654
        v7  = torch.tanh(v6) 
        v8  =v7+  1       
        v9  = v2  *        v8      
        return v9


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 40, 50)
 
__output__  = m(x1)

# Testing the initial model for correctness of operation
import numpy as np
import torch

m_initial = Model() # Initializing a new model
x1 = x1 = torch.randn(20,3,40,50) # Generating input to the model with the dimensions 3-channel 20x40x50 image. 
 
output__initial  = m_initial(x1) # Running initial model on inputs and saving output in variable named "__output__"
 
for i in range (len(__output__)):
    t1_1 = np.ones((np.shape(__output__)[i][1]),dtype=float)
    t2 = __output__[i]
    t3  = m(x1).reshape(t1_1*len(m))
    assert all([t == round(s,5) for s,t in zip(np.ndarray.flatten(__output__initial), np.ndarray.flatten(t3))])
