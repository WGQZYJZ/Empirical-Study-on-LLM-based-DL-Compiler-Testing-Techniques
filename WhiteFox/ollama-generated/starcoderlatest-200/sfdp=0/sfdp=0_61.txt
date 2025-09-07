
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        scaled_dot_product = torch.matmul(v1, v2.transpose(-2, -1)) / (math.sqrt(float(3*4)) * math.sqrt(float(64))) # The scaling factor inv_scale is set to the square root of the dimensions of the input vectors
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v1)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
