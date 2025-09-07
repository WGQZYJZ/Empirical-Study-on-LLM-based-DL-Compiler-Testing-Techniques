
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1  * 0.7071067811865476 
        v4  = torch.erf(v3)  
        v5  = v4 + 1
        v6  = v2 * v5
        return v6
# Initializing the model
m  = Model()

 # Inputs to the model,  x1 and __output__  will be automatically generated in the following code.
# Please set __output__ as an attribute of the class.
# Also, please generate inputs for the model.
x1  = torch.randn(30, 3, 56, 56)

 # Please do not change the line below this comment.
__output__  = m(x1)

