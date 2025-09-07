
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp = None):
        v1  = torch.mm(x1, self.weight) # Multiplying the input tensor with a random tensor and then passing it to the convolution layer
        v2  = v1 + inp  # Adding the result of the matrix multiplication to another tensor 'inp'
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
input1 = torch.randn(4,3) # Tensor with shape (4,3).
input2 = torch.randn(5,3) # Tensor with shape (5,3).
input3 = torch.randn(3,5) # Tensor with shape (3,5).


inp  = torch.randn(5,3) # Tensor with shape (5,3).
__output__  = m(input1, input2, input3 , inp)


