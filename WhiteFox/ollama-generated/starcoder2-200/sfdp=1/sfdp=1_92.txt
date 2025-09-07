
class Model(torch.nn.Module):
    def __init__(self, inv_scale_factor=10., dropout_p=0.2):
        super().__init__()
        self.scale = torch.nn.Parameter(inv_scale_factor * torch.ones((1)))
 
    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk  = qk / self.scale # Scale the dot product by the scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        return dropout_qk.matmul(value)

# Initializing the model
inv_scale  = torch.randn((1,))
m = Model(inv_scale[0])

