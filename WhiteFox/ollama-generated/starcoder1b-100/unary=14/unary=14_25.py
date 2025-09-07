
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 3, stride=1, padding=1)
        self.sigmoid   = torch.nn.Sigmoid()
 
    def forward(self, x2):
        v2 = self.sigmoid(self.conv_transpose(x2))
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input_tensor  = __output__ * 0.7071067811865476 # Multiply the output of the sigmoid function by 0.7071067811865476
x2            = input_tensor / (1 + torch.exp(-input_tensor))
__output__   = m(x2)

