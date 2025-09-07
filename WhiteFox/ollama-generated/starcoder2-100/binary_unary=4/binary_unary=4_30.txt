
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1) # Applying a linear transformation to the input tensor 
        v2  = v1 + other_tensor # Adding another tensor to the output of the linear transformation
        v3  = torch.nn.functional.relu(v2) # Applying the ReLU activation function to the result of the linear transformation
        return v3

# Initializing the model with keyword arguments:
m  = Model()
other_tensor = torch.rand(512,4096)
m.forward(input_tensor, other=other_tensor)

