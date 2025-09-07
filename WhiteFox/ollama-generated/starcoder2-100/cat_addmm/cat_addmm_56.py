
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
 
    def forward(self, x0):
        v2 = torch.cat([x0], dim)
        return v2
    
# Initializing the model
m  = Model()
dim = 4

# Inputs to the model
input_tensor = torch.rand(16, 32) * 8 - 1 # random numbers in range of [min; max] (float tensor). Size: (batch_size x num_of_neurons);
mat_one   = input_tensor[0:5].clone()
mat_two   = torch.rand(input_tensor.shape, requires_grad=True) # random numbers in range of [min; max] (float tensor). Size:(batch_size x num_of_neurons); 
