
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.sigmoid(x1)
        return v2
        
# Initializing the model        
m  = Model()
 
# Inputs to the model    
x1 = torch.randn(1, 640, 320).to("cuda:0") * 5 # multiplying by a constant
x2 = x1.clone().detach()
x2[:, :, :] += 5
x3 = x1 + x2
 
x_list = [v for v in (x3, x2)]

__output__  = m(torch.cat(x_list))
