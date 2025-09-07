
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 16, stride=4, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        negative_slope = -2e-1

        mask = (v1 > 0).type(torch.FloatTensor)  # v1 has only positive values so a value of 0 in the mask indicates it is negative
        t1 = v1 * negative_slope

        t2 = torch.where(mask, t1, v1)  # Select elements from v1 where the corresponding element in mask is True with their output equal to the multiplied value of the input tensor

        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 8, 64, 64)
