
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.tensor([[0.9], [1]])
        self.drop   = torch.nn.Dropout(dropout=0.2)
 
    def forward(self, query_tensor, key_tensor, value_tensor):
        vq  = torch.matmul(query_tensor, key_tensor.transpose(-2, -1))
        scaled_vq  = vq * self.scale
        svd_qk  = scaled_vq.softmax(dim=-1)
        dqv  = self.drop(svd_qk)
        vo  = torch.matmul(dqv, value_tensor)
        return vo


# Initializing the model with input tensors
qk  = torch.randn((256, 300))
key_tensor  = torch.randn((256, 800)) * 0.1
value_tensor  = torch.randn((256, 800)) * 0.9
__output__  = m(qk, key_tensor, value_tensor)

