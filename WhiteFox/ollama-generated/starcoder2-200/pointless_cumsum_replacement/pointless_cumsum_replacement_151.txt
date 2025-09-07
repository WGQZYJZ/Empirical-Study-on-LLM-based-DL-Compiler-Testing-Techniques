
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v7 = torch.full([3084], 1)
        v8 = convert_element_type(v7, torch.float64) # Convert the elements of the tensor to the specified dtype (float64 in this case)
        v9 = torch.cumsum(v8, 1).transpose_(2, 3) # Compute the cumulative sum of the elements of the tensor along dimension 1 and then transpose dimensions 2 with 3. This pattern may be reused for any shape of a tensor. 
        return v9


# Initializing the model
m = Model() 

# Inputs to the model
x2  = torch.randn(4, 8) # Creating the input as a random matrix of size 4 x 8
