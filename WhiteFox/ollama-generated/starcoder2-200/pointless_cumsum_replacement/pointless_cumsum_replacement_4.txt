
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        v1  = torch.full([arg1, arg2], 1)
        v2  = v1.convert_element_type('int32') 
        return v2
 
 # Initializing the model
 m  = Model()

 