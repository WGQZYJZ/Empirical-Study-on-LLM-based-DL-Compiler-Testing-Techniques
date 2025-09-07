
class Model(torch.nn.Module):
    def __init__(self, other1, other2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other1 # Subtract 'other' from the output of the convolution with shape [100]
        v3 = v1 + torch.arange(9).reshape([3, 3]).to(v1.device) / 3 + other2 # Add 'other' and range tensor to the output of the convolution with shape [40 x 80]
        return v2

# Initializing the model with two constants/tensors as inputs for other parameter. Here, 'other_const' is a constant of shape [] and 'other_tensor' is a random tensor of shape [100].
m = Model(torch.randn([]), torch.randn([40, 80]))

 # Inputs to the model
x2  = torch.randn([300]) # Shape [3 x 5 x 10] is invalid since 9 is not a multiple of 3 and 3 * 5 != 100 which is the number of elements in other_tensor 
 x1  = torch.randn(3, 5, 20)
__output__  = m(x1,other_const,other_tensor)

