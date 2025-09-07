
class Model(torch.nn.Module):
    def __init__(self, num_split_sizes=32):
        super().__init__()
 
    def forward(self, x1):  # input is 512x64x64
        split_tensors = torch.split(x1, self.num_split_sizes, dim=0) 
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(self.num_split_sizes))], dim=0)  # concatenate the split tensors along 3rd dimension (0-based indexing)
        return concatenated_tensor

# Initializing the model with 8 input tensors to the forward() function
m = Model(input_tensor_size=[512] + [64] * num_split_sizes,  # list of size 9: 3 numbers and then one number for each split tensor
           input_tensors=["x%d" % i for i in range(num_split_sizes)], # names for the inputs to forward()
           output_tensor="output",  # name for the output from forward()
           num_split_sizes=8)


