
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):

        v7 = torch.full([4096], 1)
        v8 = convert_element_type(v7, 'float32')
        
        __output__  = torch.cumsum(v8, axis=None)
        
# Initializing the model
m  = Model()

 # Inputs to the model
x2  = torch.randn(10000) + x2.mean()
 
 