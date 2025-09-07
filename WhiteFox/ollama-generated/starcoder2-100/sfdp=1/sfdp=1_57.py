
import torch

class Module(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._module = torch.nn.Identity()
 
    @property
    def weight(self): # This method will be used for testing
        return None
    
    @weight.setter
    def weight(self, value):  # This method will also be used for testing 
        raise NotImplementedError("This property is read-only")

    @weight.deleter 
    def weight(self):  # This method won't get invoked because the property is read only
        pass

    def forward(self, x1):
        return self._module(x1)

# Initializing a model class
class Model_v0(Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,kernel_size=5)
 
    @property 
    def weight(self): # This method will be used for testing 
        return None
    
    @weight.setter
    def weight(self, value):  
        raise NotImplementedError("This property is read-only")

    @weight.deleter
    def weight(self):  # This method won't get invoked because the property is read only
        pass
 
    def forward(self, x1):
        v1 = self._module(x1) 
        return v1 

class Model_v2(Module): 
    def __init__(self):
        super().__init__()
        
    @weight.deleter
    def weight(self): # This method won't get invoked because the property is read only
       pass
 
    def forward(self, x1):
        v1 = self._module(x1) 
        return v1 
    
# Initializing two models of class Model_v0 with different weights 
m0  = Model_v0()
m2 = Model_v2()

# Inputs to the model m0 (of class Model_v0)
x1_m0 = torch.randn(5,3,64,64) # 5 input tensors of shape [batchsize=5][height=3] x [width=64] and size=[channel=64] for a batch of 5
