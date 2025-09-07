
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.mm  = torch.addmm # Matrix multiplication operator
        
    def forward(self, x1):
        v1  = self.mm(input, mat1, mat2)
        v2  = torch.cat([v1], dim) 
        return v2


# Initializing the model
m  = Model()
__input__  = [torch.randn(300), torch.randn(800)] # 300 and 800 are randomly generated numbers between -5 and 7.9

