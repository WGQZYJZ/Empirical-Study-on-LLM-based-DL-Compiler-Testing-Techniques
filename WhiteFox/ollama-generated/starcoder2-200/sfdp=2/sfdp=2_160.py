
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_, key_, value_, scale_factor=256., dropout_p = 0.1):
 
        inv_scale_factor = torch.tensor([1/scale_factor])
        
        vq = torch.matmul(query_, key_.transpose(-2,-1))
        scaled_vq = vq * inv_scale_factor
        softmax_vq = scaled_vq.softmax(dim=-1)
        dropout_vq = torch.nn.functional.dropout(softmax_vq, p=dropout_p)

        output = dropout_vq.matmul(value_)
        return output

# Initializing the model
m  = Model()

 # Inputs to the model
query__  = torch.randn(1024, 64)
key___  = torch.randn(1024, 64)
value___  = torch.randn(1024, 512)
__output__  = m(query__, key__, value__)

