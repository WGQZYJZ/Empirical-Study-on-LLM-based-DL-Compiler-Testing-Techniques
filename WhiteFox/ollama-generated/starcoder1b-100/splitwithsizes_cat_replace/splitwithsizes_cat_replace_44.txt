
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        x_size  = torch.tensor([64, 64], dtype=torch.long, device='cpu') # Dimension of the input tensor along which we want to split the input into several sub-tensors
        y_size  = torch.tensor([32, 8],   dtype=torch.long, device='cpu') # Dimension of the output tensor along which the result of the two consecutive `torch.split` operations will be concatenated
        split_sizes = torch.cat([x_size // y_size, x_size % y_size], dim=0) # Create a concatenation that will return a new sub-tensor for each row in the input tensor (for instance, a 32*32*8 tensor). This operation takes one argument: a 1-D LongTensor with a shape of `(N)` representing the size of the batch. Each element of this Tensor is the dimension along which we want to split an input tensor. The new sub-tensor that `torch.cat` will return from `torch.split` can be different, therefore we use this concatenation along the same dimension as our split tensors.
        concatenated_tensors = []
        for i in range(len(x1)):
            x_sub  = torch.split(x1[i], split_sizes[i], dim=0) # Split the input tensor into several sub-tensors using a single line of code
            concatenated_tensor = torch.cat(x_sub, dim=0) # Concatenate the sub-tensors along the same dimension
            concatenated_tensors.append(concatenated_tensor) # Save the output of this split and concatenation
        