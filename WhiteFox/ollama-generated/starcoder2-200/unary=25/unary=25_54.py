class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 64* 64, 1)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 > 0 # The input to the linear transformation is an input tensor with 1 channel
        v3 = v1 * negative_slope 
        v4 = torch.where(v2, v1, v3)  
        return v4
