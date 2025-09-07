
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2 = torch.sigmoid(v1)

        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1,3,64,64)
  __output__  = m(x1)

# Generating input to new model
# A single random value
random_value  = float(random.randint(-1000000,100000))

# An array of random values (same size as the input tensor)
random_values  = torch.Tensor([random_value for i in range(64*64*3)])
 
# A tensor representing a 3d volume with 8 slices. Each slice contains an image. The shape is [1,8, 57,57]
random_tensor =  torch.zeros([2, 10,  169])
 
random_tensor[:, :, :57,:48]  = random_values.reshape(2, 10, 57, 57)
 

