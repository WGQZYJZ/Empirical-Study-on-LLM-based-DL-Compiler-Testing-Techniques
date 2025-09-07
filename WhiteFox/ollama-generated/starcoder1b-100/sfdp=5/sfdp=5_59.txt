
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, attn_mask):
        # v1 = self.conv(x1)  # Apply pointwise convolution with kernel size 1 to the input tensor
        # v2 = v1 * 0.5  # Multiply the output of the convolution by 0.5
        # v3 = v1 * 0.7071067811865476  # Multiply the output of the convolution by 0.7071067811865476
        v2 = torch.nn.functional.conv2d(x1, 0.5, bias=None, stride=1)  # Apply pointwise convolution with kernel size 1 to the input tensor
        v3 = torch.nn.functional.conv2d(x1, 0.7071067811865476, bias=None, stride=1)
        v4 = torch.erf(v3)
        v5 = v4 + 1
        # v6 = v2 * v5  # Multiply the output of the convolution by the output of the error function
        # v7 = v2 * v5  # Multiply the output of the convolution by the output of the error function
        # v8 = torch.tanh(v2)  # Apply the tanh function to the output of the error function
        # v9 = v7 + v4 + v8
        v6 = torch.mul(v2, v5)  # Multiply the output of the convolution by the output of the error function
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
attn_mask = torch.zeros(1, 3, 64, 64).byte().float() # Initialize an attention mask (to be filled in during training)
