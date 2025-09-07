
class Model(torch.nn.Module):
    def __init__(self, input1_shape=(4, 3), input2_shape=(3,), input3_shape=(5, 3), input4_shape=(3,))
        super().__init__()
        self.input1 = torch.nn.Linear(
            in_features=input1_shape[0] * input1_shape[1], out_features=input2_shape[0])
        self.input2 = torch.nn.Linear(
            in_features=input3_shape[0] * input3_shape[1], out_features=input4_shape[0])
 
    def forward(self, x):
        v1  = self.input1(x) # Applies a linear transformation to the input tensor 
        v2  = torch.unsqueeze(v1, dim=-1) # Unsqueeze the result of applying linear transformation
        v3  = self.input2(v2) # Applies another linear transformation to the tensor produced by unsqueezing the output of applying linear transformation
        v4  = torch.mm(x, x) + v3 # Matrix multiplication between input and input 
        return v1 * v4


# Initializing the model
input1_shape  = (28, 50)
input2_shape  = ()
input3_shape  = (7, 50)
input4_shape  = ()
m  = Model(input1_shape=input1_shape,
           input2_shape=input2_shape,
           input3_shape=input3_shape,
           input4_shape=input4_shape)

 # Inputs to the model
input  = torch.randn(*input1_shape)
__output__  = m(x1)
 