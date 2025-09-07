
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = x1.permute((0, 2, 1)) # Permute the input tensor A in this case (batch_size, seq_len, dim)
        v2 = torch.bmm(v1, self._tensor_to_permute) 
        return v2


# Initializing the model
m = Model()

# Inputs to the model. The second dimension of the input tensor is 3 and the last dimension is 5 (batch size x sequence length x input feature dim). Also please make sure that each input tensor contains at least one non-identity permutation of the other two dimensions.  
x1 = torch.randn(2, 4, 5)


# Inputs to permute function
x2_first = x1[:, :, [3]] # Swaps positions between the third and the second last (seq len, dim). Note that here the input tensor contains a non-identity permutation of its 0th and 2nd dimensions. 
x2_second = x1[:, :, [0]] # The same as above, but for the first and the third dimension of the 3rd tensor

