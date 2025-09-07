
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
 
    def forward(self, x1):  # input = torch.rand([batch_size] + [16, 32, 3])
        v1  = torch.addmm(x1, mat1, mat2) 
        v2  = torch.cat([v1], dim) 
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(batch_size] + [16, 32, 3])

 # Initializing the tensors required for the model (i.e., mat1 and mat2) 

mat1  = torch.randn([14080, 9075], requires_grad=True) # random 3D tensor of shape [batch_size] + [16, 32, 3] and size 14080 x 9075
mat2 = torch.randn(9075, 14080], requires_grad=True) # random 3D tensor of shape [batch_size] + [16, 32, 3] and size 9075 x 14080

# Initializing the optimizer to minimize the mean squared error loss between the output of the model  and target outputs.
opt  = torch.optim.SGD([mat1, mat2], lr=lr) # learning rate set at 0.1 

 