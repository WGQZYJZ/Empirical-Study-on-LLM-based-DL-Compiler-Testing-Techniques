
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.addmm(x1, mat1) # Perform a matrix multiplication between the input and matrix 1 and then add it to input
        v2  = torch.cat([v1], dim=0) # Concatenate output along dimension 0 of the first matrix multiplication
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3,48,64,64)
mat1  = torch.randn(576,49*3*3) # Matrix 1 of dimension (576 x 2209)
mat2  = torch.randn(576,1) # Matrix 2 of dimension (576 x 1)

 __output__  = m(x1)


# Model

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1  = torch.nn.Linear(80*32, 576*49*3*3) 
        self.linear2 = torch.nn.Linear(576, 40*48+49)
        self.conv = torch.nn.Conv2d(1, 3, 3)
    def forward(self, x):
        v1  = x * 2
        v2  = torch.relu(v1 + 5) 
        v3 = v2 * -0.87684901 #Multiply the output of the pointwise convolution by a constant -0.87684901
        v4 = self.conv(torch.addmm(x, mat))# Add the output to another tensor
        v5  = torch.cat([v3, v4], dim=2) #Concatenate the output of the pointwise convolution and the output of another operation along dimension 2
        v6  = torch.relu(self.linear1(torch.transpose(x)) * -0.97385305)# Apply ReLU to the output of another operation, which is then multiplied by a constant -0.97385305 
        v7  = self.linear2(v6)# Apply a linear layer
        return x * torch.relu(torch.cat([v5, v7], dim=1))


# Initializing the model and feeding in an input tensor for it
m = Model()
input_tensor = torch.randn((80,32), dtype = float)
input_tensor[input_tensor  > 0] *= 4 # Apply a multiplication to the output of the pointwise convolution

 __output__  = m(input_tensor).shape

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
       v2 = torch.erf(v3) # Apply the error function to another tensor
       v4  = self.conv(x1)# Apply a convolution operation to an input tensor
       v5  = v2 * -0.87684901# Multiply the output of the convolution by another constant  -0.87684901
       v7  = torch.addmm(v4, mat) # Add a second tensor to another tensor
       v8  = self.linear2(x)# Apply a linear layer to an input tensor 
       return x *torch.cat([v5, v7], dim=1)# Concatenate the output of the convolution and the output of another operation along dimension 1



# Initializing the model
m  = Model()

 # Inputs to the model for the model
input_tensor  = torch.randn(80*32)

 # Feeding in input tensor for the model

 __output__  = m(input_tensor).shape

