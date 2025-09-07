
class Model(torch.nn.Module):
    def __init__(self, scale_factor=10., dropout_p=0.5):
        super().__init__()
        self.scale  = torch.Tensor([scale_factor])
    
    def forward(self, qk, vk):
       scaled_qk = torch.matmul(qk, vk) * self.scale
       softmax_qk  = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
       dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.5) # Apply dropout to the softmax output
       return dropout_qk

# Initializing the model and scaling factor
scale_factor  =  1e-8
m  = Model(scale_factor=scale_factor)


# Inputs for Q, K, V tensors 
q  = torch.randn((2560,)) + 3
k  = torch.randn((2560,)) + 4
v  = torch.randn((1024, 8))
__output_qk__, __output_vk__  = m(q, k), m(q, v)

