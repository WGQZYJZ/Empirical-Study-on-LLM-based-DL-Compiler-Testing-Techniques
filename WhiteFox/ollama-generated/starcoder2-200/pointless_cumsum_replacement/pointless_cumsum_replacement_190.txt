
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t2 = torch.cumsum(torch.full([3, 4], 1), dim=1)
 
    def forward(self, x1):
        v1 = convert_element_type(x1, t2[0]) # Convert the elements of the input to the tensor filled with a constant value `1`, with the specified dtype
        return v1


# Initializing the model
m  = Model()
