
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.full([v1.size()[0], v1.size()[1]], 1.) # Create a tensor filled with the scalar value 1 with shape [v1.size()[0] * v1.size()[1]]
        v3  = convert_element_type(v2, self.conv.weight.dtype)  # Convert the elements of the tensor to dtype of conv layer's weight 
        v4  = torch.cumsum(v3, 1) # Compute cumulative sum along dimension 1 of the tensor created with the above code
        return v4


# Initializing the model
m = Model()


# Inputs to the model