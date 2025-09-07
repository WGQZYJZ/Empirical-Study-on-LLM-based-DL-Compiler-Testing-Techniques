
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scale_factor=1., dropout_p=0.5):
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v2  = v1.mul(scale_factor)
        v3  = v2.softmax(dim=-1)
        v4  = v3
        v6  = dropout(v4)
        v7  = torch.nn.functional.dropout(v5, p=0.5).matmul(value)


# Initializing the model
m  = AttentionModel()

# Inputs to the model
query_tensor  = torch.randn(1, 8, 4, 32)
key_tensor  = torch.randn(1, 8, 4, 32)
value_tensor  = torch.randn(1, 70000*50)

 # Initialize the model with different inputs. Otherwise, the previous model and input is used for inference.
x1 , x2, x3 =  torch.randint(-100,100,(4)) ,torch.randint(-98,98,(7)),  value_tensor

__output1__  = m(query_tensor)
__output2__  = m(key_tensor,x2, x3)

