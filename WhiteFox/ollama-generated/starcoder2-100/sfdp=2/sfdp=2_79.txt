
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_, key_, value_):
        inv_scale = 2 / torch.linalg.norm(key_) ** 2
        scaled_qk = qk.div(inv_scale) # scaling the dot product by an inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5) 
        output  = dropout_qk.matmul(value_)
