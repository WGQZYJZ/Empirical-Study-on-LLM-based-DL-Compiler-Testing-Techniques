
class FuseConvBN(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
        conv = torch.nn.functional.conv3d
        bn  = torch.nn.functional.batch_norm

        convbn1 = conv(input1) 
        convbn2 = bn(convbn1)

        return convbn2

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
        conv  = torch.nn.Conv3d
        convbn_func_1 = conv(input=input1)
        convbn_func_2 = torch.nn.functional.batch_norm(convbn_func_1)

        convbn_module_1 = ConvBN()
        convbn_module_2  = convbn_module_1(input1)

        return convbn_func_1

# Initializing the model
m = Model()

 # Inputs to the model: The input1 tensor has shape [B, 3, 80, 64] and 
#                    the input2 tensor is a constant with shape [B].
x1  = torch.randn(5, 3, 80, 64)
__output__  = m(x1)

