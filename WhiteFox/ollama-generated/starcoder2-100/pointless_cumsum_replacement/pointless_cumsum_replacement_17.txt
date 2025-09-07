
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.full([8,32], 1, dtype=torch.float64) 
        v2  = convert_element_type(v1, torch.int16) # Convert the elements of the tensor to a specified dtype 
        return v2 
 
 
# Initializing the model
m  = Model()
 
 # Inputs to the model
x1  = torch.randn(8,32)

 __output__  = m(x1)

## [1, 5]  ## [640, 7] ## [1290, -3]

