
class Model(torch.nn.Module):
    def __init__(self, dim1):
        super().__init__()
 
    def forward(self, x1):
        v0  = self.__random__()  # Generate a random tensor with the same size and shape as the input tensor
        v1  = torch.addmm(x1, self.__random__(dim), self.__random__())  # Perform a matrix multiplication of two tensors, add them to an input tensor, and concatenate along a specified dimension
        return v0


# Initializing model:
m  = Model(2)

# Inputs to the model