
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1, query2=None, key2=None, value2=None):
        v0 = torch.matmul(query1, key1.transpose(-2, -1))
        v3  = v0 / 1e-5
        v4  = torch.nn.functional.softmax(v3)
        v5  = torch.nn.functional.dropout(v4, p=0.1, training=True)
        v7 = value1 @ v5.transpose(-2, -1).contiguous()
        if query2 is not None and key2 is not None and value2 is not None:
            v8  = torch.matmul(query2, key2.transpose(-2, -1))
            v9  = v8 / 4e-5
            v10 = torch.nn.functional.softmax(v9)
            v11 = torch.nn.functional.dropout(v10, p=0.3, training=True)
        else:
            v7 += value2
        return v7

# Initializing the model
m  = Model()

# Inputs to the model
query_input = torch.randn(4, 8, 512).div_(torch.finfo(torch.float32).max) # 4x8x512 float32 tensor
key_input = torch.randn(4, 8, 512).div_(torch.finfo(torch.float32).max) # 4x8x512 float32 tensor
value_input = torch.randn(4, 8, 512).div_(torch.finfo(torch.float32).max) # 4x8x512 float32 tensor
__output__  = m(query_input, key_input, value_input)