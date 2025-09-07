
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear  = torch.nn.Linear(in_features=5760 + 196, out_features=14*14)
    def forward(self, x): 
        v2  = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v3  = v2 * 0.5  # Multiply the output of the convolution by 0.5

        v7  = v3 + (v3*v3*v3)*0.044715 # Add the output of the convolution to the output of the convolution cubed multiplied by 0.044715
        v8 = torch.tanh(v7) 
        v9  = v8 * -2 + 1 # Multiply the output of the hyperbolic tangent function by -2 added by 1 to the output of the hyperbolic tangent function
        v10  = self.linear(torch.cat((x, x.reshape(-1)))) # Apply linear transformation to a concatenated input tensor
        v14 = torch.max(v10, dim=-1).values 
        v15 = v3 * v9 
        return [v14, v15]
