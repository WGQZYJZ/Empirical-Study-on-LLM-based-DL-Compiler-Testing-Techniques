
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # Compute the dot product of the two input tensors
        scaled_dot_product = torch.matmul(v1, v1.transpose(-2, -1))  # (b, d, h', w') -> (b, d, h', w')
        # Divide by the square root of the dimension to obtain the attention weights
        attention_weights = scaled_dot_product.softmax(dim=-1)
        # Compute the weighted sum of the input tensor
        output = attention_weights.matmul(v1)  # (b, d, h', w') -> (b, h' * w', d').
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 64, 64)
x2 = torch.randn(3, 64, 64)
