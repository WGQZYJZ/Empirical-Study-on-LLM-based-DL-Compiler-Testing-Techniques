
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, torch.randn(2)], 0) # Concatenate two input tensors to make a 4D tensor for the bmm function.

        # Permute the concatenated 4D input tensor.
        # The shape of the permuted tensor will be [3 x 2 x 2] after swapping dimensions at index = 1 and 2 
        # to match the dimension size of torch.bmm function's first argument (2) and third argument(2).
        v2 = v1.permute(0, 2, 1) 

        # Permute a 3D input tensor to fit the third dimension for the bmm function. 
        # The shape of the permuted 4D input tensor will be [2 x 3 x 2] after swapping dimensions at index = 1 and 2
        v3 = torch.randn(5, 3) # Create a 3D tensor.
        # Permute it to fit for the third dimension of bmm function 
        v4 = v3.permute(0, 2, 1).reshape(v3.shape[0], -1)
        # Reshape the permuted input tensor from [5 x 2] to match the 3rd argument size (2 in this case). 
        return torch.bmm(v2, v4)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 2) # A tensor with shape [2 x 2]
x2 = torch.randn(3, 2) # A tensor with shape [3 x 2]


# Expected model input tensors
x1 = torch.randn(5, 2) # A tensor of size [5 x 2]
x2 = torch.randn(2, 5) # A tensor of size [2 x 5]

__output__  = m(x1), m(x2)

