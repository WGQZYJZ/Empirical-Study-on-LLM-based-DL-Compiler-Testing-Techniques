
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = convtranspose(x1) 
        v2  = v1 > 0 # Create a mask where each element is True if the corresponding element in t1 is greater than 0.
        v3  = v1 * negative_slope
        v4  = torch.where(v2, v1, v3) # Apply the where function to select elements from v1 or t3 based on the mask t2.
        return v4


m = Model()

x1 = torch.randn(1, 8, 64, 64)
