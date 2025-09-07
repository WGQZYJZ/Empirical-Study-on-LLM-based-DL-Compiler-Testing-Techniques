
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        # Concatenate 2 tensors along last dimension (axis 3) for sinking
        t1 = torch.cat([x1, x2], dim=3)

        # Reshape the concatenated tensor and apply a pointwise unary operation to the reshaped tensor 
        t2 = t1.view(4, 4)
        t3 = F.relu(t2)
        return t3

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(80, 576) # 1 input tensor with shape [80, 576] (8 batches of 4x9 images)
x2  = torch.randn(3*80*4, 9) # Another input tensor with shape [2400, 9]. This is the concatenation of several concatenated 4D tensors. 

