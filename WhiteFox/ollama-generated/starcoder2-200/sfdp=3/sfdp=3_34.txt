
class Model(torch.nn.Module):
    def __init__(self, dim1=256, dim2=256):
        super().__init__()

        self.scale = 3 * math.log(dim2) # Calculate the scale factor in the dot product
        self.linear1 = torch.nn.Linear(4*4*dim1, dim2)

    def forward(self, x1):
        # The first step in transformer models is to project the input tensor from 3 dimensions into a 2-dimensional tensor. This 2D tensor will be used as an input for the dot product operation.
        x = self.linear1(x1).reshape(-1, 4*4*self.__model__.conv_dim) # Reshape the output of linear layer to a flat 3 dimensional vector
        qk = torch.matmul(x, x.transpose(-2, -1)) # Compute dot product between input and its transpose

        scaled_qk = qk.mul(self.scale) # Scale dot product by scale factor

        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5) # Apply dropout with probability 50% to the softmax output
        output = dropout_qk.matmul(x) # Compute dot product of dropout and input

        return output

# Initializing model
m1 = Model()
# Inputs for the model (3D tensor)
input_tensor1  = torch.randn(2, 4, 4*__model__.conv_dim).contiguous().cuda()

 # Input to the model of shape (N, 784)
input_tensor2  = torch.nn.functional.linear(input_tensor1, weight=m1.__model__.linear1.weight.data).reshape(-1, __model__.conv_dim).contiguous().cuda()
 
__output__  = m1(__output__)

