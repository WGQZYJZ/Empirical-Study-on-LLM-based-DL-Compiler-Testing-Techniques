
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v1 = torch.full([2048], 1)
        v2 = convert_element_type(v1, torch.float32) # Convert the elements of the tensor to float32 datatype
        v3 = torch.cumsum(v2, dim=1) 
        return v3

# Initializing the model
m = Model()

