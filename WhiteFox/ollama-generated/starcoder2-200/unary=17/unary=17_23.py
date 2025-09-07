
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self._make_conv2d_transpose(x1)
        v2  = torch.nn.functional.relu(v1) 
        return v2
        
    def _make_conv2d_transpose(self, input):
        return F.conv_transpose2d(input=input,
                                  weight=torch.zeros([3], dtype=torch.float),
                                  stride=[1],
                                  output_padding=[0])

m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 4, 80, 96)
 
# Obtaining the outputs of each step in the model. For example, __output__ is a variable containing a tensor with shape [3] and type torch.FloatTensor.
__output__  = m(x1)

