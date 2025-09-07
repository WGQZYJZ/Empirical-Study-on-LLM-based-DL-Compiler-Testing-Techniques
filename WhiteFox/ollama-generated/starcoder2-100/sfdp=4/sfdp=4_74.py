
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
         v1  = torch.bmm(input1, input2)
         v3  = self.attention_mask * (-float('inf'))
         v4  = v1 + v3
         v5  = torch.softmax(v4, dim=-1)
         v6  = torch.bmm(v5, input2)
         return [v6]


# Initializing the model: Input1 and Input2 are two tensors. Attention mask is -inf * tensor_dim, which will be used to mask the softmax layer in forward method when computing attention weights. 
m = Model()
input1 = torch.randn(8,320) # Tensor shape  (16, 512)  
input2 = torch.randn(8,320) # Tensor shape  (16, 512)  
attn_mask = -float('inf') * torch.ones(torch.Size([input1.shape[0], input1.shape[-1]]))  

