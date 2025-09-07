
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.dropout  = torch.nn.Dropout(p=0.5)
    
    def forward(self, x):
        v1  = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 * 0.5 # Multiply the output of the convolution by 0.5 
        v3  = torch.matmul(v1 , v2 ) # Compute the dot product of two tensors
        v4  = self.dropout(v3) # Apply dropout to the output of the dot product
        return v4

m  = Model()

