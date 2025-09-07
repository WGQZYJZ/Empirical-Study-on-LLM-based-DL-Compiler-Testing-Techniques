
class SelfAttentionBlock(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = 1 / torch.sqrt(torch.tensor([64]))
 
    def forward(self, query: torch.Tensor) -> torch.Tensor:
        key  = query.transpose(-2, -1).clone().detach()
 
        scaled_dot_product  = torch.matmul(query, key) / self.scale
        
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        value  = query * attention_weights
 
        return value
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(3, 8, 5, stride=1, padding=2)
        self.conv2  = torch.nn.Conv2d(8, 4096, 7, stride=1, padding=3)
 
        self.sa_block  = SelfAttentionBlock()
 
    def forward(self, x):
        v1  = self.conv1(x)
        v2  = self.conv2(v1)
        v5  = self.sa_block(v2)
        
        return v5


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(4, 3, 608, 799)
__output__  = m(x1)
 
