
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 100)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Linear transformation of input tensor 
        v2  = other - v1 # Subtract 'other' from the output of linear transformation (v1 = other - v1)
        v3  = torch.nn.functional.relu(v2, inplace=True)# ReLU activation function
        return v3

# Initializing model and setting random seed to 4089 for reproductibility.
other  = np.random.rand() # Other is 0.751657214978557 in this example
m  = Model().cuda()
seed(4089)

# Generating input to the model
x1  = torch.randn(3, 32).cuda() # 3 random tensors of size (3 x 32), which will be passed as input to the model during testing

 