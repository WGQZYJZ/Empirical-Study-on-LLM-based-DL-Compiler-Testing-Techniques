
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor
        v3 = F.relu(v2) 
        return v3


# Initializing the model 
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # The size of input tensor for this model
__output__  = m(x1)

# Adding another tensor as a parameter
m2 = Model().cuda()
 
# Inputs to the model with 2 inputs instead of only one.
x1 = torch.randn(3, 3, 64, 64).cuda() # The size of input tensors for this model. You need to create two additional input tensors each of size [batch_size x channels x H x W] where H and W are the height/width (dimension 2/3) of the convolutional layer
x1 = torch.randn(4, 3, 64, 64).cuda() # This is an example of input tensors with batch sizes larger than one. You need to create two additional input tensors each of size [batch_size x channels x H x W] where the value of batch_size is larger than one and H and W are the height/width (dimension 2/3) of the convolutional layer
__output1__, __output2__ = m(x1, otherTensor1, otherTensor2)

