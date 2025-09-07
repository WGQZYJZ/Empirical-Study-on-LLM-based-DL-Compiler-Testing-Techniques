
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        l1 = self.linear(x1) # Apply linear transformation to the input tensor
        l2 = l1 + 3          # Add 3 to the output of the linear transformation 
        l3 = torch.clamp_min(l2, 0)       # Clamp the output of addition operation to minimum value of zero 
        l4 = torch.clamp_max(l3, 6)      # Clamp the output of previous operation to maximum value of six
        l5 = l4 / 6               # Divide the output of previous operation by 6 
        return l5


# Initializing model with random weights and bias terms:
m1= Model()

# Inputs to the model for generating valid outputs. This can be any tensor of the same shape as inputs required in previous example models. The output tensors generated here must match the expected format for input into m1
x1 = torch.randn(2, 3)


__output1a__ = m1(x1)


# Initializing model with fixed weights and bias terms:
m2= Model()
m2.linear[0].weight=torch.tensor([[5.,4.,7.]]) # Weights of the linear layer 
m2.linear[0].bias=torch.tensor([3]) # Bias term in the linear layer 

__output1b__ = m2(x1)

