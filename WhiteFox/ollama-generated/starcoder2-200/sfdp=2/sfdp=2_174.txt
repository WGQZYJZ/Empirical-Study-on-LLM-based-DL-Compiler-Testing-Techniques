
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale_factor=1., dropout_p=0., **kwargs):
 
        vq = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        vsq = vq.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        vsq_sm = vsq.softmax(dim=-1)  # Apply softmax to the scaled dot product
        vdsqk  = torch.nn.functional.dropout(vsq_sm, p=dropout_p) # Apply dropout to the softmax output
        vo = vdsqk.matmul(value)  # Compute the dot product of the dropout output and the value
        return vo


m = Model()


# Inputs for this model
qk  = torch.randn(2048, 12563)
key  = torch.randn(768, 9, 2345)
value  = torch.randn(2048, 20, 3276)


qk_out__ = m(qk, key, value)
