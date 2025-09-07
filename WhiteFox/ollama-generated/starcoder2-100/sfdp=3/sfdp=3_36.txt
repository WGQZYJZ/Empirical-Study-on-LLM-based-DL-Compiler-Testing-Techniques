
class Model(torch.nn.Module):
    def __init__(self, d_model=1280):
        super().__init__()
 
        self.scale  = torch.nn.Parameter(data=torch.ones(d_model), requires_grad=True)
        self.dropout_p = nn.Dropout(0.1)
 
    def forward(self, query, key, value):
        scale_factor = self.scale
        # ...

        qk  = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk  = qk * scale_factor
        softmax_qk  = scaled_qk.softmax(dim=-1) 
        dropout_qk = dropout(softmax_qk, p=dropout_p)
 
        output  = torch.bmm(dropout_qk, value)
        return output


# Initializing the model
m  = Model()
 
# Inputs to the model
query  = torch.randn(6400, 128, 3072) # Shape: [6400 x 128 x 3072]
key  = torch.randn(6400, 128, 3072) # Shape: [6400 x 128 x 3072]
value  = torch.randn(6400, 128, 512) # Shape: [6400 x 128 x 512]
__output__  = m(query, key, value)

