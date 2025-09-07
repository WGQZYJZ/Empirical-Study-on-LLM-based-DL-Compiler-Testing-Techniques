
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key  = torch.randn(128, 64)
        self.query  = torch.randn(1024, 768)
        self.value  = torch.randn(32, 512)
 
    def forward(self):
        scale_factor  = 1 / math.sqrt(self.key.shape[0]) 
        v1 = torch.nn.functional.dropout(torch.matmul(self.query, key.transpose(-2, -1)) / scale_factor).div_(inv_scale_factor) # Scale the dot product by the inverse scale factor
        v3  = self.value.div_(inv_scale_factor) # Divide the value tensor by the inverse scale factor
        return v1 * 0.5 + v3

# Initializing the model
m  = Model()
 
# Inputs to the model
key  = torch.randn(256, 512)
query  = torch.randn(8192, 768)
value  = torch.randn(4096, 512)
 