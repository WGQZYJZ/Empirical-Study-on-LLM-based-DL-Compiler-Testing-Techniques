
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v0 = torch.matmul(x1, x2) 
        return v0 
 
# Initializing the model 
m = Model()
 
# Inputs to the model  
input_x1 = torch.randn([8, 4], requires_grad=True) # Input tensor of size [batchsize, dim]
input_x2 = torch.randn([5, 4])                     # Input tensor of size [batchsize*num_head*dim, num_head*dim]. The first dim is batchsize, and the second dimension is the total number of heads in parallel processing.
__output__  = m(input_x1, input_x2)

