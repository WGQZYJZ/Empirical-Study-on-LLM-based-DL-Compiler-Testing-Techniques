
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = self.__output__
        t287594464939375792  = torch.nn.functional.conv_transpose2d(v0, 8)
        t1477974785749160042  = t287594464939375792 * v0
        t217735457447135797   = torch.pow(t1477974785749160042, 3)
        t23803959085654507    = v0 + t217735457447135797 * torch.tensor(float(.044715)) 
        t24984374860083814    = .7978845608028654
        t1886825606783784879  = torch.tanh(t23803959085654507) + v0 
        t26528096356860391    = .5
        return t23803959085654507 * v0


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3, 3, 64, 64) # It will be used to generate input for the previous model that is not included in the current model.
