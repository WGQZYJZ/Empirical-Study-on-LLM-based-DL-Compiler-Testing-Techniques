
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        scaled_dot_product = torch.matmul(x1, x2).div(float(math.sqrt(float(len(x1.shape)))))
        attention_weights = scaled_dot_product.softmax(-1)
        output = attention_weights * x2
        return output


# Initializing the model
m  = Model()


# Inputs to the model
q = torch.randn(3, 64, 64, dtype=torch.float32, requires_grad=True)
k1 = torch.randn(8, 3, 64, 64, dtype=torch.float32, requires_grad=True)
v1 = torch.randn(8, 8, 64, 64, dtype=torch.float32, requires_grad=True)
