
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1  *  0.5 
        v3  = (v1 * v1).view(-1, 1, 84, 76)[..., None] # View the result of the previous operation into an intermediate tensor with shape `(1, 1, 84, 76)`, and add a new axis to the shape
        v3  = (v3 * v3).view(-1, 84*84)[:, None] # View the result of the previous operation into another intermediate tensor with shape `(2903750, 1)`
        v3  = (v3 * v3).view(len(x), 3, 64, 64)[..., None].sum(-1) # Convert back to the original shape after viewing and then sum across the 4th dimension. The shape becomes `(2903750, 8)`
        v4  = v3 * 0.044715 
        v5  = v1 + v4  
        v6  = v5 * 0.7978845608028654 
        v7  = torch.tanh(v6)
        v7  = v7 + 1 
        v8  = v2  * v7 
        return v8

# Initializing the model