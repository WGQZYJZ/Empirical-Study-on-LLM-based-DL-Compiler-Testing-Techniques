
class Model(torch.nn.Module):
    def __init__(self, shape=32, size=1024):
        super().__init__()
 
    def forward(self, input1):
        v0 = torch.split(input1, shape)  # Split the input tensor into several tensors along dimension 1 of shape 32x1
        concatenated_tensor = torch.cat([v0[i] for i in range(shape)], dim=1) 
        return concatenated_tensor.sum()

# Initializing the model
m  = Model()
 
# Input to the model
x = np.random.randn(32, shape).astype(np.float32) # Generate random input tensor with dimensions (32 x 1024) 
__output__  = m(torch.from_numpy(x))

