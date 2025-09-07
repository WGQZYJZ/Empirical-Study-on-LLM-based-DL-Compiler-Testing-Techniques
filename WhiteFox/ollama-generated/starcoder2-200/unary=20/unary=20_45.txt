
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.sigmoid(v3)
        return v4
 
 
class Upsample(torch.nn.Module):
 	def __init__(self):
		super().__init__()

	def forward(self, input):
 		output  =  F.conv_transpose2d(input, self.weight, padding=0)
		return output

m1  = Upsample()
m2  = Model()

 # Initializing the models with different weights and bias

m3 = nn.ConvTranspose2d(8, 64, kernel_size=7, stride=(1))
w1 = torch.ones([3,8,5,5])
b1  = torch.zeros([3])
m1.weight  = w1
m1.bias  = b1

 # Inputs to the models
 
x2  = torch.randn(64, 7, 10)


 __output__  = m2(x1)
 __output__  = m3(x2)
