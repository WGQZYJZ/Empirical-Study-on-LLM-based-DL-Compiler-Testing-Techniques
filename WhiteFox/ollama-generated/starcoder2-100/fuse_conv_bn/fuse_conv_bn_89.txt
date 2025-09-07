
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        conv = torch.nn.functional.conv3d(input1, self._weight)  # _weight is a private attribute that we are not interested in
        bn = torch.nn.functional.batch_norm(conv)
        output = conv + bn
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(2,3,400,50,60)# Conv and BN is on the first channel 
__x1_permute = x1.transpose(1,2) # Permuted tensor, swapped last two dim
x2  = torch.randn(2,3,784)
x2  = torch.reshape(x2,(2,-1))# Flattening the input tensor to be used as the main input of the linear layer


# Outputs from the model