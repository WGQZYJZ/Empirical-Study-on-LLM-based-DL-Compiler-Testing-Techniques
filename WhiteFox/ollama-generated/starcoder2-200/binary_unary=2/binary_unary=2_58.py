
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1) - self.__output__
        v2  = v1 + 1 # Add 1 to the output of the convolution by subtracting another tensor or scalar "other" from it
        v3  = torch.relu(v2) 
        return v3


# Initializing the model
m  = Model() 

# Inputs to the model (one of them should not be equal to the output of the previous one, that is why the input tensor should contain more than one element). 
x1 = torch.randn(5, 8, 64, 32)


# Obtain the initial and final output of the model after applying the first and second convolutions. 
o1  = m(x1)[0] # We take only one element for simplicity
o2  = __output__[0]
assert o1 != o2, 'You must use a new tensor here!'

# Obtain the initial and final output of the model after applying the first and second convolutions. The first output should be larger than the initial one.
o3  = m(x1)[0] # We take only one element for simplicity
assert o3 > o2, 'The first output of the first convolution is less than its initial value!'