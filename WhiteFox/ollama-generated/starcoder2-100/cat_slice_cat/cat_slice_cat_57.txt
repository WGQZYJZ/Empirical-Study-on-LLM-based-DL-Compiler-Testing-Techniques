
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensors):
 
        # Concatenate the tensors along axis 1 to form the first output tensor of this layer
        t0 = torch.cat(input_tensors, dim=1)
        
        # Slice the first output tensor along axis 1 (The dimension with index i becomes 9223372036854775807 elements long)
        t1 = t0[:, 0:9223372036854775807]
        
        # Slice the second output tensor along axis 1 (The dimension with index i becomes size elements long)
        t2 = t1[:, 0:size]
 
        # Concatenate the first and second outputs tensors 
        t3 = torch.cat([t0, t2], dim=1)

        return t3


# Initializing the model
m = Model()
 
# Input to the model should be a list of 5 tensors
x1 = [torch.randn(i*size+j+709483649, i+j*2, j+k*3) for i in range(5)]
 
