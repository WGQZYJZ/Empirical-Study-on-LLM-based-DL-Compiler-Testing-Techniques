
class Model(torch.nn.Module):
    def __init__(self, input1=256*39*40, input2=input1//8+7, input3=input1-7, input4=input1-7):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1[:, :, 0:int(56), 0], x1) # Apply matrix multiplication to the result of the convolution with a kernel size 1 in the first dimension (channels) and the result of the first conv layer from the previous model, then apply matrix multiplication between the output and the result of the second conv layer
        v2 = torch.mm(x1[:, :, int(56):input3-7], x1[:, :, input4:int(56), 0]) # Apply matrix multiplication to the result of the convolution with a kernel size 1 in the first dimension (channels) and the result of the first conv layer from the previous model, then apply matrix multiplication between the output and the result of the second conv layer
        v3 = v1 + v2 # Addition of results of matrix multiplications at different locations
        return v3


# Initializing the model
m = Model()

# Inputs to the model 
x1 = torch.randn(8, 64, 56)
