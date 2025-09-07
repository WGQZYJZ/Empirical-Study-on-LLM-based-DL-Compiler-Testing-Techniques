
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # The model will have a different output tensor than previous one.
        v1 = torch.nn.Linear()(x1)  # Apply linear transformation to the input tensor
        v2 = v1 + other_tensor
        v3 = torch.relu(v2)  # Apply ReLU activation function to the result 
        return v3


# Initializing the model
m  = Model()
 
# Input tensors for the model
x1, x2 = torch.randn(1, 8), torch.randn(10, 9)
other_tensor = torch.randn(5, 7) # a tensor that will be added to the output of the linear transformation before applying ReLU activation function


# Outputs from the model on each input tensors 
__output1__, __output2__= m(x1), m(x2)

