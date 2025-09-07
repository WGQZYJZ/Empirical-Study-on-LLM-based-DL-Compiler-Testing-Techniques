
class Model(torch.nn.Module):
    def __init__(self, num1, num2):
        super().__init__()
        self.input3  = torch.randn(num1, num2) # Create a randomly generated 2-D tensor with size num1 by num2 for input3 
        self.input4  = torch.randn(num2, num1) # Create a randomly generated 2-D tensor with size num2 by num1 for input4
        self._linear  = torch.nn.Linear(int(self.input3.nelement() / (num1 * num2)), int(self.input4.nelement() / (num2 * num1)))
 
    def forward(self, x):
        v1  = self._linear(torch.mm(x[0], torch.mm(self.input3, x[1]))) # Apply linear transformation on matrix multiplication between the two matrices. The input shape is (num1*num2,num2*num1)
        return [v1] + [None for _ in range((len(x)-1))]


# Initializing the model 
m = Model(784, 300).eval() # Use 60K randomly generated numbers as input to initialize the input tensors. The output shape of the linear transformation is (num1*num2, num2*num1) which means the input tensor has size 2.
 

# Inputs to the model
x = [m(torch.randn([784]))] # Apply a 3-D convolution operation on randomly generated numbers with shape 784 by 1 for the input tensors

