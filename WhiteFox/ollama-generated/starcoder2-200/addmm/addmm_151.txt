
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp):
        v1 = torch.mm(tensor1, tensor2) 
        return v1 + inp
        
# Initializing the model
m  = Model()

 # Inputs to the model 
inp  = torch.randn(6400).view(-1, 800)
 
x1 = torch.randn(800, 5792)
tensor2  = torch.randn(38, 432)
tensor1  = torch.zeros((inp.shape[-1], tensor2.shape[1]))
 
 # Initializing input tensors
tensor2_ = tensor2[idx]
x1_= x1[idx]
 
__output__  = m(inp)

