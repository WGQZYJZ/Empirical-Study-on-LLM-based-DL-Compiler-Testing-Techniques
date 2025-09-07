
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 3, 2) # swaps first and third dimensions of the first input tensor; then permutes it to be of shape (1, 4, 8)
        v2 = torch.bmm(v1, x2) # multiplies matrix A[1x4] by matrix B[4x8], resulting in a 1x8 matrix. This is used as the main input for the second linear transformation

        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 5) # shape of x1 should be (batch_size, number_of_input_dimensions_in_first_input_tensor, number_of_input_dimensions_in_second_input_tensor)
x2  = torch.randn(4, 8)     # shape of x2 is (number_of_input_dimension_in_second_input_tensor1xN, number_of_input_dimension_in_second_input_tensorNxB)


# Initializing the model 
m = Model() 

# Inputs to the model 
input_tensorA  = torch.randn(20, 5, 784) # shape of input_tensorA should be (batch_size=20, number_of_input_dimensions1=5, number_of_input_dimension2=784). Here, we used the bmm method to apply a linear transformation to the matrix A. We permute first, using .permute() method so that, the permuted tensor is of size (batchsize, 3, 7)
input_tensorB = torch.randn(20, 5, 784) # shape of input_tensorA should be same as above


__output__  = m(input_tensorA, input_tensorB)

