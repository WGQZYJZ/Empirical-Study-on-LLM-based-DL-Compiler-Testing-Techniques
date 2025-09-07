
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).float() # Convert boolean tensor to float tensor
        v3 = v1 * 0.5
        v4 = torch.where((v2 == True), v1, v3) # For each element in the boolean tensor, if the element is True, choose the corresponding element from the output of the linear transformation, otherwise choose the corresponding element from the output of the multiplication by the negative slope
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(200, 3) # A tensor with shape (200, 3) will be generated. The size will vary according to the random input tensor dimensions provided by users.
