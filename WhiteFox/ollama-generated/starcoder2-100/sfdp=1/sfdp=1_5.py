
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 32
        self.softmax = torch.nn.Softmax(dim=-1)
        self.dropout = torch.nn.Dropout(0.8, False)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        v1  = torch.matmul(query, key.transpose(-2,-1)) / math.sqrt(32) # [batch_size x head x len x len]
        v2  = self.softmax(v1)
        v3  = self.dropout(v2)
        v4  = torch.matmul(v3, value) # [batch_size x head x len x dim]
        return v4

# Initializing the model
m = Model()

# Input to the model<|end_of_input|>
i0 = torch.randn([256, 8, 128])
i1 = torch.randn([256, 8, 37])
i2 = torch.randn([256, 4096, 32*2, 5*8])
__output__  = m(i0, i1, i2)
