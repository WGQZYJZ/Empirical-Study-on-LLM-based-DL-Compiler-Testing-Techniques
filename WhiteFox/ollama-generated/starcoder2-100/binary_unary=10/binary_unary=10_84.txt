
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(48*32, 10)
 
    def forward(self, x1, y1):
        v1 = self.linear(x1) 
        v2 = v1 + y1 # Add another tensor to the output of the linear transformation
        v3 = F.relu(v2) # Apply the ReLU activation function to the result
        return v3

# Initializing the model
m  = Model()

# Input tensors for the model with sizes 64x512 and other tensor is of size 64x10. Note that the two tensors are not identical, i.e., they do not contain the same number of elements. 64 is the batch dimension in these 2 tensors.

x = torch.randn(64*512) # Input Tensor 1 (size: 64 x 512)  
y = torch.randint(0, 3, size=(64*10)) # Input tensor other with size 64 x 10 
__output__  = m(x, y).shape  # Output of the model which will contain 64 x 10

