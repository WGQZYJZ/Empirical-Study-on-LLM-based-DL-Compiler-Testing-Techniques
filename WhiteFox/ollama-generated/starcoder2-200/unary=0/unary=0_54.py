
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1): 
        v1   = self.conv(x1)
        v2   = v1  *   0.5
        v3   = v1 ** 3
        v4   = torch.rsqrt((v3 + 1)) # Use the rsqrt function to take square root of the result of the previous operation cubed and add 1, and then take reciprocal of that number using rsqrt()
        v5   = tanh(v2 * (v4 + 1.0))
        v6   = v3 * v4 # Take result of the previous operation cubed multiplied by the result of the previous operation cubed multiplied by 0.7978845608028654 and then add 1 to this value and multiply it with 0.5
        v7   = v6 + v3 
        v8   = v7 * 0.5 # Divide the result of the previous operation by 2 using division operator. 
        __output__    =  v5 * v8
        return v5

