
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32*32*8, 64)
 
    def forward(self, x1):
        v1  = self.linear(x1.reshape(-1, 32*32*8)) # linear transformation on input tensor to make it of the size 64 
        v2  = v1 + other_tensor  # Add another tensor with size 64 in the output (different from the input)
        v3  = torch.nn.functional.relu(v2)  # Apply ReLU activation function on the result
        return v3

# Initializing and running the model with random tensors

i1, i2, i3  = np.random.randn(64*64), np.random.randn(32), np.random.randn(8) # Random input tensors of size (64, 64), (32,) and (8,) respectively

model_before = Model()
o1_b         = model_before((torch.Tensor(i1)).reshape(-1).reshape(64*64)) 

other        = np.random.randn(int(np.prod(o1_b))) # Random tensor of size (64*64)
model       = Model() # The model to be modified in the next cell 
model(torch.Tensor(i1).reshape(-1).reshape(32*32*8)).shape, other_tensor.shape<jupyter_output><empty_output>