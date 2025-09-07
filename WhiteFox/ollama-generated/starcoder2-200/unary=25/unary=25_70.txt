
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.flatten(x1) 
        v2  = self._thresholding(v1)
        v3  = (v1 - v2).reshape((v1.shape[0], 7)) # reshape to original shape
        return v3 

    def _thresholding(self, x):  
        out_tensor = torch.zeros_like(x) 
        threshold = torch.mean(torch.where(torch.lt(x, 0), x , torch.zeros_like(x)))
        out_tensor = out_tensor + x - threshold
        return out_tensor

# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn((256,3,4))  
 