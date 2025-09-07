
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1): # note that you can also add another input tensor here to check its usage later on.
        v1 = torch.cat((x1, y1), 2)

        t1a  = v1.permute(-1, -3, -2).contiguous() 
        t2b  = v1[:, :, ::-1]
        t3c  = v1[:, :][:,::-1]
        t4d  = torch.bmm(v1[:], v1[:,:,:].transpose(-2,-3))
        t5e  = torch.einsum("ijk->jik", v1)

        return t1a + t2b + t3c + t4d + t5e


# Initializing the model
m  = Model() # note that the shape of input tensors and number of inputs are flexible, you should choose suitable ones.
__input_A__   = torch.randn(801,60)[:,::2]
__input_B__   = torch.randn(735459168, 2)
__output__    = m(__input_A__, __input_B__) # you should feed the initial input tensors to the model as its arguments. 
