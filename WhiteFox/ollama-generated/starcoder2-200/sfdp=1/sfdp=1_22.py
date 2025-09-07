
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, query, key, value, dropout_p=0., scale_factor=1.):
        scale = 2**34
        
        qk  = torch.matmul(query, key) / (scale/ scale_factor)
        scaled_qk  = qk.div(scale* scale_factor).softmax(-1)
        dropout_qk  = scaled_qk.dropout(p=dropout_p)
        output  = dropout_qk * value
        
        return output
        

# Initializing the model
m  = Model()

# Inputs to the model (Note that, we are using different parameters in this example, so that we ensure that we get a different example.)
query  = torch.randn(4096)
key  = torch.randn(256, 1024)
value  = torch.randn(8388608, 768)
        

