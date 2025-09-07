
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        _, _, h  = x1.size() 
        _, _, w  = x2.size() 
        split_sizes = [int((w/4)*(h/4)), int((3*w/8)*(h/4))]
        splitted_tensors = torch.split(x1, split_sizes, dim=2) # Split the input tensor into two tensors along the channel dimension of the shape (H/4, W/4). The split operation can also be performed along any other dimensions that are present in x1 and have matching sizes.
        concatenated_tensor = torch.cat(splitted_tensors[0] for 0 in range(len(split_sizes)), dim=2) # Concatenate the two tensors from the previous step, reshaping them to the original shape (H/4*W/8). The concatenation operation can also be performed along any other dimensions that are present in x1 and have matching sizes.
        concatenated_tensor = torch.cat(splitted_tensors[0] for 0 in range(len(split_sizes)), dim=2) # Concatenate the two tensors from the previous step, reshaping them to the original shape (H/4*W/8). The concatenation operation can also be performed along any other dimensions that are present in x1 and have matching sizes.
        return concatenated_tensor


# Initializing the model
m = Model()
 
x1  = torch.randn(1, 32, 64)
x2  = torch.randn(1, 80, 75)
__output__  = m(x1, x2)

