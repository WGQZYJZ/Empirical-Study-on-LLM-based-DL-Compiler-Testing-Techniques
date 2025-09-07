
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, x2) # Matrix multiplication on input tensors 
        return v1 + v3


# Initializing the model 
m = Model()
 
__inputs__ = {
    'input1': torch.randn(4096, 512), 
    'input2': torch.randn(512, 768)  # Passing random input tensors 
}
 
 __outputs__  = m(**inputs) # Feeding the inputs to the model
 
__inp__ = torch.randn(4096, 3000) # Creating another input tensor
 
__output__  = m(__inputs__, __inp__)

