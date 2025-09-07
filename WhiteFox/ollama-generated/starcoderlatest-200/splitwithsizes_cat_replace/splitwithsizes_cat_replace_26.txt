
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.split(x1, 2)  # Apply pointwise convolution with kernel size 2 to the input tensor
        s1 = torch.cat([t1[0], t1[2]]) # Split the output of the previous convolution in two parts: the first half and the second half
        concat_tensors  = torch.cat([s1, t1[1]], dim=1)  # Concatenate the split tensors along dimension 1
        v6  = concat_tensors  * 0.7071067811865476  # Multiply the output of the convolution by 0.7071067811865476
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2, 2)
