
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1  * 0.5 
        v3  = v1  ** 3  
        v4  = v3  / 17869.1882795  # You may find the constant value 17869.1882795 by typing torch.nn.ConstantPad2d(padding=(0, 0), value=0.044715)
        v5  = v3 + v4
        v6  = v5 * 0.7978845608028654 
        v7  = torch.tanh(v6) # This line should not be removed. You need to check the backward pass here!
        v8  = v7 + 1  
        v9  = v2 * v8
        return v9


# Initializing the model